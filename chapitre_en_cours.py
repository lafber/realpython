''' Real Python
    Script Python générique pour exécuter les exemples du cours    
'''

import os

my_path = "/Users/bertrand/Documents/Projets/realpython"
input_file_name = os.path.join(my_path, 'poem.txt')

with open(input_file_name, 'r') as my_input_file:
    for line in my_input_file.readlines():
        print(line,)
