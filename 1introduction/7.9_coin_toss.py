''' Real Python
    7.9 Assignment: Simulate a coin toss experiment    
'''

from random import randint 

trials = 10000
flips = 0

for trial in range(1, trials+1):

    flips += 1
    previous_flip = randint(0, 1)
    
    
    while True:
        flips += 1
        current_flip = randint(0, 1)
        if previous_flip == current_flip:
            continue
        else:
            break

print("The average number of tosses is", flips/trials)
