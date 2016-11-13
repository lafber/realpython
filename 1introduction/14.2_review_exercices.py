''' Real Python
    It is a well-documented fact that the number of pirates in the world is 
    correlated with a rise in global temperatures. Write a script pirates.py that 
    visually examines this relationship
'''

### Module(s) importation ###
import os
import csv

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


### Functions ###


### Parametrage ###
source_path = 'practice_files'
source_file = os.path.join(source_path, 'pirates.csv')

output_path = 'output'

temperatures = [ ]      # list for the average world temparatures
pirates = [ ]           # list for the pirates numbers
years = [ ]             # list foor the years
    
############
### MAIN ###
############


with open(source_file, 'r') as source_data : 
    my_csv_reader = csv.reader(source_data)
    next(my_csv_reader)
    for year, temp_value, pirates_nb in my_csv_reader :
        print("Year {} the average world temperature was {} and the pirates number {}".format(year, temp_value, pirates_nb))
        temperatures.append(temp_value)
        pirates.append(pirates_nb)
        years.append(year)

# print(temperatures, pirates, years)

plt.plot(pirates, temperatures, "r-o")

plt.title('Pirates in the world by rise in global temperatures')
plt.xlabel('Number of pirates')
plt.ylabel('Average world temperatures (C°)')

# annotate points with years
for i in range(0, len(years)):
    plt.annotate(str(years[i]), xy=(pirates[i], temperatures[i]))

plt.savefig(os.path.join(output_path, 'pirates_temp.png'))