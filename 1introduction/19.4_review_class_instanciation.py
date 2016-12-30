''' Real Python
Review exercises:
Using the same Dog() class, instantiate three new dogs, each with a different 
age. Then write a function called, get_biggest_number() , that takes any number 
of ages ( *args ) and returns the oldest one.
'''

### Module(s) importation ###

### Functions ###
def get_biggest_number( *args ):
    oldest = 0
    for element in args:
        if int(element) > oldest:
            oldest = int(element)
    return oldest


### Parametrage ###


### Classes definition ###
class Dog(object):
    
    # Class Attribute
    species = 'mammal'
    
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

############
### MAIN ###
############

# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))
    
# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))

pumpy = Dog("Pumpy", 7)

print("The oldest dog is {} years old".format(get_biggest_number(philo.age, mikey.age, pumpy.age)))