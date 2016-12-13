''' Real Python
Open the phone_list.py file from the exercises folder, which contains a list of dictionaries
find all the people with the last name "Hardy" or a first name starting with the 
letter J. Output their first names, last names, and phone numbers.
'''

### Module(s) importation ###
import re 
from phone_list import data

### Functions ###

### Parametrage ###


############
### MAIN ###
############

# first name starting with the letter J
# OR last name "Hardy"
target = re.compile(r'^(J\w+) (\w+)|^(\w+) (Hardy)') 

for contact in data:
    result = target.search(contact['name'])
    if result:
        print("First name {}, Last name {}, Phone {}".format(
                 result.group(3) if result.group(1) == None else result.group(1), 
                 result.group(4) if result.group(2) == None else result.group(2),
                 contact['phone']))
    