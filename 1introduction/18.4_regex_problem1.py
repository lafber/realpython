''' Real Python
18.4 Problem 1 regular expression 

'''

### Module(s) importation ###
import re 

### Functions ###

### Parametrage ###

############
### MAIN ###
############

validation = re.compile(r'(\w+)@(\w+).(\w+)')

email = input("Please enter your email: ")

while not validation.search(email):
    
    print("Please enter your email correctly!")
    email = input("Please enter your email: ")
    
print("\nYour email is {}!".format(email))