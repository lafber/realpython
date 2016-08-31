''' Real Python
    4.2 Find a String in a String
    3. Write and test a script that accepts user input using input() , then displays the result of trying to find() a particular letter in that input
'''

user_phrase = input('What is your name ? ')

letter = 'A'
position = user_phrase.upper().find(letter)

print("Your name has the letter {} in position {}".format(letter.upper(), position))
