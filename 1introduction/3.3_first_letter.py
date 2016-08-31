''' Real Python
    3.3 Assignment: pick apart your user's input 
'''

input_password = input("Tell me your password please : ")

first_letter = input_password[0:1].upper()

print('Your password begins with', first_letter, 'and is', len(input_password), 'long')
