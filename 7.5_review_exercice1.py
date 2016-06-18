''' Real Python
    7.5 review exercice 1
    Use a break statement to write a script that prompts the users for input repeatedly, only ending when the user types "q" or "Q" to quit the program; a common way of creating an infinite loop is to write while True: .
    
'''

while True:    # boucle infinie
    user_input = input("Enter a phrase to capitalize or exit with Q: ")
    if user_input.upper() == 'Q':
        break
    else:
        print(user_input.upper())
