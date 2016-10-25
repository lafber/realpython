''' Real Python
    Script Python générique pour exécuter les exemples du cours    
'''

import mechanicalsoup

my_browser = mechanicalsoup.Browser( )
login_page = my_browser.get("https://realpython.com/practice/login.php")
login_html = login_page.soup

# select the form and fill in its fields
form = login_html.select("form")[0]
form.select('input')[0]['value'] = 'zeus'
form.select('input')[1]['value'] = 'ThunderDude'

profiles_page = my_browser.submit(form, login_page.url) #submit form

print(profiles_page.url)
print(profiles_page.soup)

for link in profiles_page.soup.select('a'):
    print('Address:', link['href'])
    print('Text:', link.text)