''' Real Python
    7.4 Assignment: Find the factors of a number    
'''

def is_divisible(number, divisor):
    if number%divisor == 0:
        return True
    else:
        return False


user_integer = int(input("Enter a positive integer: "))

for i in range(1, user_integer+1):
    if is_divisible(user_integer, i):
        print('{} is a divisor of {}'.format(i, user_integer))
        

