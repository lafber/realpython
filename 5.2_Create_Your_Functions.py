''' Real Python
    5.2 Create Your Own Functions
        
'''

def square(number):
    """ renvoie le carré d'un nombre
        entier ou réel. """
    sqr_num = number ** 2
    return sqr_num


input_num = 5
output_num = square(input_num)

print(output_num)
