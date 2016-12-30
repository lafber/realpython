''' Real Python
Review exercises

'''

### Module(s) importation ###

### Functions ###

### Parametrage ###


### Classes definition ###

class Pet(object):
    
    pets = []
    
    def __init__(self, *args):
        self.pets = args 
        self.count_pets()
        
    def count_pets(self):
        self.pets_nb = len(self.pets)
        
    def list_pets(self):
        
        pet_list = ''
        for pet in self.pets:
            pet_list += pet.name + ' is ' + str(pet.age) + '. ' 
        
        return pet_list
        
    def describe(self):
        print("I have {} dogs : {} And they're all mammals, of course."
                .format(self.pets_nb, self.list_pets()))

    def walk(self):
        for dog in self.pets:
            print(dog.walk())

# Parent class
class Dog(object):
    
    # Class attribute
    species = 'mammal'
    is_hungry = True
    
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
        
    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
    # instance method
    def eat(self):
        self.is_hungry = False
        
    # instance method
    def walk(self):
        return "{} is walking!".format(self.name)

# child class (inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
        
# child class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


############
### MAIN ###
############

# create my pets list with 3 dogs 
my_pets = Pet(Dog('Tom', 6), Dog('Mike', 7), Dog('Larry', 9))
my_pets.describe()
my_pets.walk()