''' Real Python
    7.3 Control the Flow of Your Program- review exercice
    Write a script that prompts the user to enter a word using the input() function, stores that input in a variable, and then displays whether the length of that string is less than 5 characters, greater than 5 characters, or equal to 5 characters by using a set of if , elif and else statements.
    
'''

user_word = str(input("Enter a word please: "))

word_length = len(user_word)

if word_length < 5:
    print("Your word length is less than five characters")
elif word_length == 5:
    print("Your word is five characters long")
else:
    print("Your word is more than 5 characters long")

    
