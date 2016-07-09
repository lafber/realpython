''' Real Python
    8.4 Store Relationships in Dictionaries Review exercises
'''

# 1. Create an empty dictionary named birthdays
birthdays = {}

# 2. Enter data in dictionnary
'''birthdays['Luke Skywalker'] = '5/24/19'
birthdays['Obi-Wan Kenobi'] = '3/11/57'
birthdays['Darth Vader'] = '4/1/41'
'''

# 6. bonus  dictionnary with dict( )
birthdays = dict([('Luke Skywalker', '5/24/19'), ('Obi-Wan Kenobi', '3/11/57'), ('Darth Vader','4/1/41')])


# 3.

if not 'Yoda' in birthdays:
    birthdays['Yoda'] = 'unknown'

if not 'Darth Vader' in birthdays:
    birthdays['Darth Vader'] = 'unknown'

# 4.
def display_birthday(birthdays_dict):
    for person in birthdays_dict:
        print(person, birthdays_dict[person])

# 5.Delete 'Darth Vader' from the dictionary
del(birthdays['Darth Vader'])


### MAIN
display_birthday(birthdays)
