''' Real Python
    Script Python générique pour exécuter les exemples du cours    
'''

import sqlite3

    
people_values = (
        ('Ron', 'Obvious', 42),
        ('Luigi', 'Vercotti', 43),
        ('Arthur', 'Belling', 28)
)                
    


with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
    c.executescript("""
        DROP TABLE IF EXISTS people;
        CREATE TABLE people(firstname TEXT, lastname TEXT, age INT);
                    """)

    c.executemany("INSERT INTO people VALUES(?,?,?)", people_values)
    
    
    c.execute("SELECT FirstName, LastName FROM People WHERE age > 30")

    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
