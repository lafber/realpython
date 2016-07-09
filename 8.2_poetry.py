''' Real Python
    8.2 Assignment: Wax poetic

    Write a script poetry.py that will generate a poem based on randomly chosen words and a pre-determined structure.
    
'''

import random

def getRandomlyElements( list, quantity ):
    """ From a list take randomly the quantity elements """
    n = 1
    elements = []
    
    while n <= quantity:
        word = random.choice(list)
        if not word in elements:
            n = n + 1
            elements.append(word)
        
    return elements


def makePoem( ):
    
    nouns_selected = getRandomlyElements( nouns, 3)
    verbs_selected = getRandomlyElements( verbs, 3)
    adjectives_selected = getRandomlyElements( adjectives, 3)
    adverbs_selected = getRandomlyElements( adverbs, 1)
    prepositions_selected = getRandomlyElements( prepositions, 2)
    
    poem = "A {adjective1} {noun1}\n\
A {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}\n\
{adverb1}, the {noun1} {verb2}\n\
the {noun2} {verb3} {preposition2} a {adjective3} {noun3}".format(adjective1=adjectives_selected[0], adjective2=adjectives_selected[1], adjective3=adjectives_selected[2],
                                                                  noun1=nouns_selected[0], noun2=nouns_selected[1], noun3=nouns_selected[2],
                                                                  verb1=verbs_selected[0], verb2=verbs_selected[1], verb3=verbs_selected[2],
                                                                  adverb1=adverbs_selected[0],
                                                                  preposition1=prepositions_selected[0], preposition2=prepositions_selected[1])

    return poem
    
# the Vocabulary lists
nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

### MAIN
print(makePoem( ))
