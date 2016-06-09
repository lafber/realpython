''' Real Python
    Functions Summary 5.3

    Write a function multiply() that takes two numbers as inputs and multiplies them
    together, returning the result; test your function by saving the result of multiply(2, 5) in a new variable and printing it   

'''

def multiply( nb1,nb2 ):
    return nb1 * nb2

user_nb1 = int(input('Enter a number: '))
user_nb2 = int(input('Enter another number :'))

print(multiply(user_nb1,user_nb2))
