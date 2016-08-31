''' Real Python
    Review exercises chapitre 10 
    
'''

'''
1. Read in the raw text file poem.txt from the chapter 10 practice files and display each line by looping over them individually, then close the file;
we'll discuss using file paths in the next section, but for now you can save your script in the same folder as the text file
''' 
print('Exercice 1:\n')
my_file = open('poem.txt', 'r')

for line in my_file.readlines():
    print(line, end='')

my_file.close()


'''
2. Repeat the previous exercise using the with keyword so that the file is closed automatically after you're done looping through the lines
'''

print('\n\nExercice 2:\n')

with open('poem.txt', 'r') as my_file2:
    for line in my_file2.readlines():
        print(line, end='')

'''
3. Write a text file output.txt ... 


print('\n\nExercice 3.1:\n copying poem.txt to output.txt')

my_file = open('poem.txt', 'r')
my_output = open('output.txt', 'w')

for line in my_file.readlines():
    my_output.writelines(line)

my_file.close()
my_output.close()
'''


'''
3.2
'''

with open('poem.txt', 'r') as my_poem, open('output2.txt', 'w') as my_output2:
    for line in my_poem.readlines():
        my_output2.writelines(line)

'''
4. Re-open output.txt and append an additional line of your choice to the end of the fileon a new line
'''
with open('output2.txt', 'a') as output2:
    output2.writelines('\nAnd the incredulous horse run\nThe gorilla running after it')
