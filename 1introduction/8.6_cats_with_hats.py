''' Real Python
    Assignment: Cats with hats
    
'''


# cats are in a list
# cats with hat have a "hat" otherwise a False. 
cats = {}

# populate the hundred cats without hat
for i in range(1,101):
    cats[i] = False


# MAIN

# 100 rounds to puts hat on or remove 
for round in range(1,101):

#   Circle around the hundred cats
    for cat, hat in cats.items():
        # cat number is divisible 
        if cat % round == 0:
            # cat has a not hat put one
            if hat == False:
                cats[cat] = True
            else:
                cats[cat] = False

# Output final cats
for cat, hat in cats.items():
    print('Cats n°{} hat : {}'.format(cat, hat))
