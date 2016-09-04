''' Real Python
Assignment: Create a high scores list from CSV data
'''

### Module(s) importation ###
import os
import csv

### Parametrage ###
my_path = 'practice_files/'

scores = {}

### MAIN ###

# Reading the score file 
with open(os.path.join(my_path, 'scores.csv'), 'r') as score_file:
    my_csv_reader = csv.reader(score_file)

    for user, score in my_csv_reader:
        scores[user] = score  # creating the dictionnary
        

# Printing the scores sorted by user name
for user in sorted(scores):
    print(user, scores[user])

