# Liskov Substitution Principle

"""
Liskov Substitution Principle states that "Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program."
"""


class Car:
    def __init__(self, type):
        self.type = type

class PetrolCar(Car):
    def __init__(self, type):
        self.type = type


car = Car("SUV")
car.properties = {"Color": "Red", "Grear": "Auto", "Capacity": 6}
print("Car properties:", car.properties)

petrol_car = PetrolCar('Sedan')
petrol_car.properties = ("Blue", "Manual", 6)
print("Petrol car properties:", petrol_car.properties)

"""
As we can see here, there is no standard specification to add properties of the Car and it is left to the developers to implement in the way convenient to them. 
One developer may implement it as a Dictionary and another may implement it as a Tuple and thus it can be implemented in multiple ways.

Now, let’s say that there is a requirement to find all Red colored cars. 
Let’s try to write a function that would take all the Cars and try to find out Red cars based on the implementation of the object of the “Car” Super Class.
"""

cars = [car, petrol_car]

def find_red_cars(cars):
    red_cars = 0
    for car in cars: 
        if car.properties['Color'] == 'Red':
            red_cars += 1
    print(f"Number of Red Cars: {red_cars}")

# find_red_cars(cars) # this will break the program

"""
As we can see here, we are trying to loop through a list of car objects. 
And here we break the Liskov Substitution principle as we cannot replace Super type Car’s objects with objects of Subtype PetrolCar in the function written to find Red cars. 

A better way to implement this would be to introduce setter and getter methods in the Superclass Car using which 
we can set and get Car’s properties without leaving that implementation to individual developers. 
This way we just get the properties through a setter method and its implementation remains internal to the Superclass. 
"""

class Car:
    def __init__(self, type):
        self.type = type
        self.car_properties = {}

    def set_properties(self, color, gear, capacity):
        self.car_properties = {"Color": color, "Gear": gear, "Capacity": capacity}

    def get_properties(self):
        return self.car_properties

class PetrolCar(Car):
    def __init__(self, type):
        self.type = type
        self.car_properties = {}

car = Car("BMW")
car.set_properties("Red", "Auto", 6)

petrol_car = PetrolCar("Jaguar")
petrol_car.set_properties("Blue", "Sedan", 4)

cars = [car, petrol_car]

def find_red_car(cars):
    red_cars = 0
    for car in cars:
        if car.get_properties()['Color'] == 'Red':
            red_cars += 1
    print(f"Number of Red Cars:", red_cars)

find_red_car(cars)

