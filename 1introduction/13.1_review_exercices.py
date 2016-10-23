''' Real Python
Review exercises
'''

### Module(s) importation ###
from urllib.request import urlopen
import re     # regular expression

### Functions ###

### Parametrage ###
source_url ='https://realpython.com/practice/dionysus.html'

############
### MAIN ###
############

# chapter 13.1 review ex 1 : Write a script that grabs the full HTML from the page dionysus.html
print('-'*10, "Review exercice 1 chapter 13.1", '-'*10)

html_page = urlopen(source_url)
html_text = html_page.read( ).decode('utf-8')

print (html_text)


# chapter 13.1 review ex 2 : 
print('-'*10, "Review exercice 2 chapter 13.1", '-'*10)

name_start = html_text.find('<h2>') + len('<h2>')
name_end = html_text.find('</h2>') 
print(html_text[name_start:name_end])


color_start = html_text.find('Favorite Color')
color_end = html_text.find('</center>') 

print(html_text[color_start:color_end])


# chapter 13.1 review ex 3 : 
print('-'*10, "Review exercice 3 chapter 13.1", '-'*10)
# from correction 
for tag in ["Name:.*?[\n<]", "Favorite Color:.*?[\n<]"]:
    match_results = re.search(tag, html_text)
    # Remove the "Name: " or "Favorite Color: " label from first result
    result = re.sub(".*: ", "", match_results.group())
    # Remove extra spaces and newline padding along with opening HTML tag
    print(result.strip(" \n<"))