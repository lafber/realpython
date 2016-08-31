''' Real Python
    7.6 Recover from error : review exercice 
    Write a script that repeatedly asks the user to input an integer, displaying a message to "try again" by catching the ValueError that is raised if the user did not enter an integer; once the user enters an integer, the program should display the number back to the user and end without crashing    
'''

while True:
    
    try:
        user_input = int(input("Enter an integer please: "))
        print("Your integer is {}".format(user_input))
        break
    
    except ValueError:
        print('An integer please, try again')
