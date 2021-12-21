# WebScrapAmazon
WebScraping Amazon to get prices of the items.
## The project is made with the intention of getting the prices of the products on amazon.
There are 3 functionalities in the project.
* Add more items.
* Check status.
* Show trend.

Let us understand what each feature means.
1. Add more item: Here you will be asked to enter the url of the product you wish to track. Once out enter the url it will stored in the file. You can add more using this option. The file where the url stored is Other\UrlTrack.txt
2. Check status: This feature checks the price from the website and stores it in the file output.txt. Sometimes the parser might not work. This is a drawback, but t works most of the time. You can restart the terminal if you don't get price or name of the product.
3. Show trend: This feature will show the trend of the prices. Everytime check status is used the data is stored and used to plot a graph that shows price trend over a period of time.

## How to get started.
1. Clone the repository in the local machine.
2. Open terminal inside the repository.
3. Type the following command to install the dependencies and packages.
> pip install -r requirements.txt

Incase of error use:
> python -m pip install -r requirements.txt

4. Then run `main.py`
> python main.py

5. You'll see the features.
