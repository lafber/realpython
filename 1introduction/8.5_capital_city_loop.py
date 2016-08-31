''' Real Python
    Assignment: Capital city loop 2
    
'''

# importing state capital
from capitals import capitals_dict
# importing random package
import random


# Grad a random state and capital
def get_random_capital( capitals ):
    state = random.choice( list(capitals.keys()))
    capital = capitals[state]
    return state, capital



### MAIN

state, capital = get_random_capital( capitals_dict )

# Guess the capital
while True:
    user_respons = input('Guess the state capital to win or exit : ').lower( )
    if user_respons == 'exit':
        print('Goodbye. The capital was {} of the state {}.'.format(capital, state))
        break
    elif user_respons == capital.lower( ):
        print('Correct')
        break
    else:
        print('Nope, try again.')
