''' Real Python
    Functions Summary 5.3

    Write a cube() function that takes a number and multiplies that number by itself twice over, returning the new value; test the function by displaying the result of calling your cube() function on a few different numbers
    
'''

def cube(input_number):
    return input_number * input_number * input_number


user_number = int(input('Enter a integer to cube : '))

print(cube(user_number))
