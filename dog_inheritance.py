       ''' Create a base class called Animal with the following attributes: name and species. 
It should also have a method speak() that returns a general message like "This animal makes a sound.". 
Then, create a derived class Dog that inherits from Animal and overrides the speak() method to return "Woof!". 
Finally, create an instance of Dog and print the name, species, and the result of the speak() method.
You are creating a game where different types of characters can be used. Create a base class Character that has attributes name and health. 
The class should also have a method attack() that prints "Attacking!". 
Then, create a derived class Wizard that adds an attribute mana and overrides the attack() method to print "Casting a spell!". 
Finally, create an instance of Wizard and demonstrate both name, health, and mana attributes. '''


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "This animal makes a sound."

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def speak(self): # Method overriding
        return "woof!"


# Creating an instance of a class
dog = Dog("popy", "Mammal")
print(f"The name of the dog is {dog.name}")
print(f"The species is {dog.species}")
print(f"It says {dog.speak()}")



