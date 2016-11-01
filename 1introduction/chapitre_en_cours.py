''' Real Python
    Script Python générique pour exécuter les exemples du cours    
'''

import mechanicalsoup
from time import sleep

my_browser = mechanicalsoup.Browser( )

# Obtain 1 stock quote per minute for the next 3 minutes


for i in range(0,3):
    
    page = my_browser.get("https://fr.finance.yahoo.com/q?s=^fchi")
    html_text = page.soup
    
    # return a list of all tags where 
    my_tags = html_text.select("#yfs_l10_^fchi")
    
    my_price = my_tags[0].text
    
    print("The current price of CAC40 is: {}".format(my_price))
    if i< 2:
        sleep(60)