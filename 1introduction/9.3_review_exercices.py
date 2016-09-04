''' Real Python
    Review exercises

    
'''

import os
import csv

my_path = 'practice_files'


#1 Write a script that reads in the data from the CSV file pastimes.csv located in the chapter 9 
# practice files folder, skipping over the header row
print('1', '-'*20)

with open(os.path.join(my_path,'pastimes.csv'), 'r') as my_file:
    my_csv = csv.reader(my_file)
    next(my_csv)
    for row in my_csv:
        print(row)
        
#2 Display each row of data (except for the header row) as a list of strings
print('2 & 3', '-'*20)

with open(os.path.join(my_path,'pastimes.csv'), 'r') as my_file:
    my_csv = csv.reader(my_file)
    next(my_csv)
    for person, pastime in my_csv:
        print('{} favorite pastime is {}'.format(person, pastime))
        
    
#3 Add code to your script to determine whether or not the second entry in each row
# (the "Favorite Pastime") converted to lower-case includes the word "fighting" using
# the string methods find() and lower()
        if pastime.lower().find('fighting') != -1:
            print('and this pastime include fighting')
            
#4 Use the list append() method to add a third column of data to each row that takes
# the value "Combat" if the word "fighting" is found and takes the value "Other" if
# neither word appears
print('4', '-'*20)

with open(os.path.join(my_path,'pastimes.csv'), 'r') as my_file:
    my_csv = csv.reader(my_file)
    next(my_csv)
    for row in my_csv:
        if row[1].lower().find('fighting') != -1:
            row.append('Combat')
        else:
            row.append('Other')
        print(row)


#5 Write out a new CSV file categorized pastimes.csv to the Output folder with the
#  updated data that includes a new header row with the fields "Name", "Favorite Pastime", 
#  and "Type of Pastime"
print('5', '-'*20)

with open(os.path.join(my_path,'pastimes.csv'), 'r') as my_file, open(os.path.join(my_path,'pastimes_plus.csv'), 'w') as my_output:
    
    my_csv = csv.reader(my_file)
    my_output = csv.writer(my_output)
    
    my_output.writerow(['Name', 'Favorite Pastime', 'Type of pastime'])
    
    next(my_csv)
    for row in my_csv:
        if row[1].lower().find('fighting') != -1:
            row.append('Combat')
        else:
            row.append('Other')
        
        my_output.writerow(row)
