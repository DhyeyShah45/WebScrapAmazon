import requests
import pytz 
from bs4 import BeautifulSoup
from datetime import datetime
from matplotlib import pyplot as plt
import csv
from item import *

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

# Finds the title of the item
def find_title(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser') 
    try:
        # title = soup.find("span", {"id":"productTitle",'class_':'a-size-large product-title-word-break'})
        title = soup.find('span',id="productTitle")
        title_name = title.string.strip()
        
    except AttributeError:
        title_name = "Not Available"
    
    # print(title_name)
    return title_name

# Finds the price of the item
def find_price(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml') 
    # print(soup.prettify())
    try:
        # price = soup.find("span", {"id":"priceblock_ourprice"})
        price = soup.find('span',class_="a-offscreen")
        price_float = float(price.string[1:].replace(",","")) 
        # print(price)
    except AttributeError:
        price_float = 0

    # print(price_float)
    return price_float

# Store the URL's in a file.
def dealing_with_urls(url):
    try:
        with open('Other\\UrlTrack.txt','r+') as file:
            for line in file:
                if line == url:
                    return
            file.write(url)
            return
    except FileNotFoundError:
        with open('Other\\UrlTrack.txt','w') as file:
            file.write("")
            dealing_with_urls(url)

# Write date,price in csv file
def write_info(objectlist):
    now = datetime.now()
    localtz_info = pytz.timezone("Asia/Kolkata")
    localtime = now.astimezone(localtz_info)
    date = localtime.strftime("%d/%m/%Y %H:%M")
    
    for obj in objectlist:
        try:
            with open('Other\\'+obj.title[:20]+'.csv','a',newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow([date,obj.price]) 
                # print(obj.price)
                continue
        except FileNotFoundError:
            with open('Other\\'+obj.title[:20]+'.csv','w') as file:
                continue
    return
    
# The function that will give out the details of objects
def print_to_outputfile(objectlist):
    with open('output.txt','w') as ofile:
        for obj in objectlist:
            ofile.write(obj.title+'\n') 
            ofile.write(str(obj.price)+'\n') 
            ofile.write(obj.url+'\n')
            ofile.write('\n') 
    print("Please check the output.txt file for the status.")
    return

# Makes the objects of items
def make_objects():
    objectlist = []
    with open('Other\\UrlTrack.txt','r') as file: 
        for url in file:
            title = find_title(url.rstrip())
            price = find_price(url.rstrip())
            objectlist.append(item(title,price,url.rstrip()))
    return objectlist

# Main functionality
def check():
    olist = make_objects()
    print_to_outputfile(olist)
    write_info(olist)
    return olist

# Show trend will just generate the graph from the excel.
def show_trend():
    for obj in check():
        with open('Other\\'+obj.title[:20]+'.csv') as file:
            price = []
            date = []
            csv_reader = csv.reader(file)
            for line in csv_reader:
                price.append(line[1])
                date.append(line[0])
        plt.style.use('seaborn')
        plt.plot_date(date,price,label=obj.title[:20],linestyle="solid")
        plt.legend()
        # plt.savefig("Figures\\"+obj.title[:20]+".png")
        plt.show()
    return