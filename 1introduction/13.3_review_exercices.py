''' Real Python
Review exercises chapitre 13.3
'''

### Module(s) importation ###
import mechanicalsoup
from bs4 import BeautifulSoup

### Functions ###

### Parametrage ###
source_page = 'https://realpython.com/practice/login.php'


############
### MAIN ###
############

my_browser = mechanicalsoup.Browser( ) # instanciation du navigateur


# chapter 13.3 review ex 1 :Use MechanicalSoup to provide the correct username 
# "zeus" and password "ThunderDude" to the login page submission form 
print('-'*10, "Review exercice 1 chapter 13.3", '-'*10)

login_page = my_browser.get(source_page)
login_html = login_page.soup 

#selection du formulaire et remplissage
login_form = login_html.select('form')[0]
login_form.select('input')[0]['value'] = 'zeus'
login_form.select('input')[1]['value'] = 'ThunderDude'

profiles_page = my_browser.submit(login_form, login_page.url)
print(profiles_page.url)

# chapter 13.3 review ex 2 : Using Beautiful Soup, display the title of the 
# current page to determine that you have been redirected to profiles.html
print('-'*10, "Review exercice 2 chapter 13.3", '-'*10)
print(profiles_page.soup.title.text)


# chapter 13.3 review ex 3 : Use mechanize to return to login page by going 
# "back" to the previous page
print('-'*10, "Review exercice 3 chapter 13.3", '-'*10)
login_page = my_browser.get(source_page)
print(login_page.soup.title.text)

# chapter 13.3 review ex 4 : Provide an incorrect username and password to 
# the login form
print('-'*10, "Review exercice 4 chapter 13.3", '-'*10)

#selection du formulaire et remplissage
login_form = login_html.select('form')[0]
login_form.select('input')[0]['value'] = 'zeus'
login_form.select('input')[1]['value'] = 'HadesSucks'

profiles_page = my_browser.submit(login_form, login_page.url)
if profiles_page.soup.text.find("Wrong username or password!") != -1:
    print("Login Failed.")
else:
    print("Login Successful.")