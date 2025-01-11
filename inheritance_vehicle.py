       '''Exercise: Vehicle and Car Hierarchy
Create a base class called Vehicle with the following:

Attributes:
brand (string): The name of the brand.
color (string): The color of the vehicle. 
Methods:
describe(): Prints: This is a [color] [brand] vehicle.
Create a subclass called Car that inherits from Vehicle and adds the following:

Attributes:
number_of_doors (int): Number of doors.
Methods:
describe(): Overrides the parent method and prints: This is a [color] [brand] car with [number_of_doors] doors.
Create another subclass called Truck that inherits from Vehicle and adds the following:

Attributes:
cargo_capacity (int): Capacity in kilograms.
Methods:
describe(): Overrides the parent method and prints: This is a [color] [brand] truck with a cargo capacity of [cargo_capacity] kg.
Test your classes by:

Creating an instance of Vehicle.
Creating an instance of Car.
Creating an instance of Truck.
Calling the describe() method for each of them.'''


class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def describe(self):
        print(f"This is a {self.color} {self.brand} vehicle")


    def honk(self):
        print("Beep! Beep!")


class Car(Vehicle):
    def __init__(self, brand, color, number_of_doors):
        super().__init__(brand, color)
        self.number_of_doors = number_of_doors

    def describe(self):
        print(f"This is a {self.color} {self.brand} car with {self.number_of_doors} doors.")


'''Create another subclass called Truck that inherits from Vehicle and adds the following:

Attributes:
cargo_capacity (int): Capacity in kilograms.
Methods:
describe(): Overrides the parent method and prints: This is a [color] [brand] truck with a cargo capacity of [cargo_capacity] kg.
Test your classes by:

Creating an instance of Vehicle.
Creating an instance of Car.
Creating an instance of Truck.
Calling the describe() method for each of them.''' 

class Truck(Vehicle):
    def __init__(self, brand, color, cargo_capacity):
        super().__init__(brand, color)
        self.cargo_capacity = cargo_capacity



    def  describe(self):
        print(f"This is a {self.color} {self.brand} truck with a cargo capacity of {self.cargo_capacity} kg.")


# Testing the classes
object_name1 = Vehicle("yellow","toyota")
object_name1.describe()
object_name1.honk()

object_name2 = Car("yellow","toyota", 4)
object_name2.describe()
object_name2.honk()

object_name3 = Truck("yellow","toyota", 10000)
object_name3.describe()
object_name3.honk()












