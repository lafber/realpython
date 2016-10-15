''' Real Python
Review exercises
<ce qu’il faut faire>
'''

### Module(s) importation ###
import sqlite3

### Functions ###

### Parametrage ###

############
### MAIN ###
############

# 1. Create a database table in RAM named Roster that includes the fields Name , Species and IQ

connection = sqlite3.connect(':memory:')
c = connection.cursor()

c.execute("CREATE TABLE roster( name TEXT, species TEXT, iq INT) ")

roster_values = ( 
    ('Jean-Baptiste Zorg', 'Human', 122),
    ('Korben Dallas', 'Meat Popsicle', 100),
    ("Ak'not", 'Mangalore',-5)
    
    )
    
c.executemany("INSERT INTO roster VALUES(?,?,?)", roster_values)

c.execute('UPDATE roster SET species=? WHERE name=?', ('Human', 'Korben Dallas'))

c.execute("SELECT name, iq FROM roster WHERE species='Human' ")
for row in c.fetchall():
    print(row)
    
    
    