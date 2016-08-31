''' Real Python
    5.3 review exercices 1 to 3   
'''


''' Exercice 1 : Write a for loop that prints out the integers 2 through 10, each on a new line, by using the range() function 

for i in range(2, 11):
    print(i)
'''


''' Exercice 2 : Use a while loop that prints out the integers 2 through 10 (Hint: you'll need to create a new integer first; there isn't a good reason to use a while loop instead of afor loop in this case, but it's good practice...)


i = 2

while(i < 11):
    print(i)
    i += 1
'''

''' Exercice 3 : Write a function doubles() that takes one number as its input and doubles that number three times using a loop, displaying each result on a separateline; test your function by calling doubles(2) to display 4, 8, and 16
'''

def doubles(number):
    for i in range(1,4):
        number = number * 2
        print(number)

user_number = int(input('Enter a number to process: '))

doubles(user_number)
