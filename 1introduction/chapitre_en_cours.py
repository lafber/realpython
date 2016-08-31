''' Real Python
    Script Python générique pour exécuter les exemples du cours    
'''

my_input_file = open("hello.txt", "r")
print("Line 0 (first line):", my_input_file.readline())

my_input_file.seek(0) # jump back to beginning
print("Line 0 again:", my_input_file.readline())
print("Line 1:", my_input_file.readline())

my_input_file.seek(8) # jump to character at index 8
print("Line 0 (starting at 9th character):", my_input_file.readline())

my_input_file.seek(10, 1) # relative jump forward 10 characters
print("Line 1 (starting at 11th character):", my_input_file.readline())

my_input_file.close()
