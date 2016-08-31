''' Real Python
    Chapitre 8 : list review exercices
    
'''

# 1. Create a list named desserts that holds the two string values "ice cream"and "cookies"
desserts = ['ice cream', 'cookies']

# 2. Sort desserts in alphabetical order, then display the contents of the list
desserts.sort( ) 
print("My desserts are:", desserts)

# 3. Display the index number of "ice cream" in the desserts list
print("the ice cream is in position {}".format(desserts.index('ice cream')))

# 4. Copy the contents of the desserts list into a new list object named food
food = []
food.extend(desserts)

# 5. Add the strings "broccoli" and "turnips" to the food list
food.append('broccoli')
food.append('turnips')

# 6. Display the contents of both lists to make sure that "broccoli" and "turnips" haven't been added to desserts
print("My food are:", food)
print("My dessserts are:", desserts)

# 7. Remove "cookies" from the food list
food.remove('cookies')

# 8. Display the first two items in the food list by specifying an index range
print('the first two food available are', food[0:2])

# 9
my_breakfast = "cookies, cookies, cookies"
breakfast = my_breakfast.split(", ")
print('Available breakfasts are: ', breakfast)

#10

def output_below_20( number_list ):
    for number in number_list:
        if number <= 20 and number >= 1:
            print(number)

output_below_20([2, 4, 8, 16, 32, 64])



