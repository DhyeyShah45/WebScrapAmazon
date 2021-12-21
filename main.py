from function import *
option = int(input("What you want to do?\n1. Add new items.\n2. Check the status.\n3. See the price trend.\n"))
if option == 1:
    more = True
    while(more):
        # Get the url input to be tracked from user.
        url = input("Please copy the URL of the item to tracked from the browser: ")+("\n")
        # adding new urls and prices
        dealing_with_urls(url)
        # adding more urls
        answer = input("Want to add more items? (y/n): ")
        if answer == 'y':
            more = True
        else:
            more = False
            print("Thanks for using this application")
elif option == 2:
# checking the status of prices. Just analysis is sent out.
    check()
elif option == 3:
# Gives the pices trend of the items.
    show_trend()