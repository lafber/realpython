''' Real Python
    7.7 Simulate Events and Calculate Probabilities
   
'''

from random import randint

'''
    Review exercice 1
    Write a script that uses the randint() function to simulate the toss of a die, returning a random number between 1 and 6. 

#Simulate the toss of a die
print("Your die roll is {}".format(randint(1, 6)))
'''

'''
    Review exercice 2
    Write a script that simulates 10,000 throws of dice and displays the average number resulting from these tosses.
'''

def roll_d6():
    return randint(1, 6)

number_roll = 0
total = 0

for roll in range(1, 10001):
    total += roll_d6()
    number_roll += 1

print("the average number after {} rolls is {}".format(number_roll, total/number_roll))
