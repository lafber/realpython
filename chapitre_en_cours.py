''' Real Python
    Script Python générique pour exécuter les exemples du cours    
'''


try:
    number = int(input("Enter an non-zero integer: "))
    print("10 / {} = {}".format(number, 10.0/number))
except ValueError:
    print("You did not enter an integer.")
except ZeroDivisionError:
    print("You cannot enter 0.")
