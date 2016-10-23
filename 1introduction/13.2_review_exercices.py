''' Real Python
Review exercises chapitre 13.2 
'''

### Module(s) importation ###
from bs4 import BeautifulSoup
from urllib.request import urlopen

### Functions ###

### Parametrage ###
my_source = 'https://realpython.com/practice/profiles.html'


############
### MAIN ###
############


my_respons = urlopen(my_source) 
my_html = my_respons.read()
my_soup = BeautifulSoup(my_html, 'html5lib')

# chapter 13.2 review ex 1 : Write a script that grabs the full HTML from the page profiles.html
print('-'*10, "Review exercice 1 chapter 13.2", '-'*10)
print(my_soup)


# chapter 13.2 review ex 2 : Parse out a list of all the links ...
print('-'*10, "Review exercice 2 chapter 13.2", '-'*10)

for anchor in my_soup.find_all('a'):
    print(anchor['href'])


# chapter 13.2 review ex 3 : Parse out a list of all the links ...
print('-'*10, "Review exercice 3 chapter 13.2", '-'*10)


for anchor in my_soup.find_all('a'):
    print('.'*10, anchor['href'], '.'*10,)
    my_follow_source = 'https://realpython.com/practice/' + anchor['href']
    my_follow_html =  urlopen(my_follow_source).read()
    my_follow_soup = BeautifulSoup(my_follow_html, 'html5lib')
    print(my_follow_soup.get_text())
