'''You are creating a game where different types of characters can be used. 
Create a base class Character that has attributes name and health. 
The class should also have a method attack() that prints "Attacking!". 
Then, create a derived class Wizard that adds an attribute mana and overrides the attack() method to print "Casting a spell!". 
Finally, create an instance of Wizard and demonstrate both name, health, and mana attributes.'''

class Character:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def attack(self):
        print("Attacking")


class Wizard(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def attack(self):
        print("Casting a spell!")


wizard = Wizard("langovick", "sick", 30)
print(f"The name of the wizard is {wizard.name}")
print(f"The health of the wizard is {wizard.health}")
print(f"mana of the wizard is {wizard.mana}")

stubborn = Character("lango","sick")
stubborn.attack()




        
