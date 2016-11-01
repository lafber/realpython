''' Real Python
Review exercises chapter 13.4
'''

### Module(s) importation ###

### Functions ###

### Parametrage ###
source_page = "https://fr.finance.yahoo.com/q?s=^fchi"


############
### MAIN ###
############


import mechanicalsoup
from time import sleep

my_browser = mechanicalsoup.Browser( )

# Obtain 1 stock quote per minute for the next 3 minutes


for i in range(0,3):
    
    page = my_browser.get(source_page)
    html_text = page.soup
    
    # return the stock price
    my_price = html_text.select("#yfs_l10_^fchi")[0].text
    
    #return the time of the stock 
    my_time = html_text.select("#yfs_t10_^fchi")[0].text
    
    
    print("The current price of CAC40 at {} is: {}".format(my_time, my_price))
    if i< 2:
        sleep(10)