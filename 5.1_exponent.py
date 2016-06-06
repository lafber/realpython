''' Real Python
    5.1 Assignment: Perform calculations on user input

    Write a script called exponent.py that receives two numbers from the user and displays the result of taking the first number to the power of the second number. A sample run of the program should look like this 
    
'''

user_base = float(input('Enter a base: '))
user_exponent = int(input('Enter an exponent: '))

print("{} to the power of {} = {}".format(user_base, user_exponent, user_base**user_exponent))

