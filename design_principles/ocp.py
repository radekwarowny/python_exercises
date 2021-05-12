# Open-Closed Principle 

"""
Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modifiction.
"""

"""
In the below example we have a class DiscocuntCalculator that has a property to hold the type of apparel. 
It has a function that calculates the discount based on the type of apparel and returns the new cost after deducting the discount amount.
"""

# Wrong approach

from enum import Enum
class Products(Enum):
    SHIRT = 1
    TSHIRT = 2
    PANT = 2

class DiscountCalculator:
    def __init__(self, product_type, cost):
        self.product_type = product_type
        self.cost = cost

    def get_discounted_price(self):
        if self.product_type == Products.SHIRT:
            return self.cost - (self.cost * 0.10)
        elif self.product_type == Products.TSHIRT:
            return self.cost - (self.cost * 0.15)
        elif self.product_type == Products.PANT:
            return self.cost - (self.cost * 0.25)


dc_shirt = DiscountCalculator(Products.SHIRT, 100)
print(dc_shirt.get_discounted_price())

dc_tshirt = DiscountCalculator(Products.TSHIRT, 100)
print(dc_tshirt.get_discounted_price())

dc_pant = DiscountCalculator(Products.PANT, 100)
print(dc_pant.get_discounted_price())

"""
This design breaches the Open-Closed principle because this class will need modification if 
a). A new apparel type is to be included and 
b). If the discount amount for any apparel changes. 
"""

# Right approach

from abc import ABCMeta, abstractmethod

class DiscountCalculator:

    @abstractmethod
    def get_discounted_price(self):
        pass

class DiscountCalculatorShirt(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.10)

class DiscountCalculatorTshirt(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.15)

class DiscountCalculatorPant(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        return self.cost - (self.cost * 0.25)

dc_Shirt = DiscountCalculatorShirt(100)
print(dc_Shirt.get_discounted_price())

dc_Tshirt = DiscountCalculatorTshirt(100)
print(dc_Tshirt.get_discounted_price())

dc_Pant = DiscountCalculatorPant(100)
print(dc_Pant.get_discounted_price())

"""
As shown in the above example we have now a very simple base class DiscountCalculator that has a single abstract method get_discounted_price. 
We have created new classes for apparel that extends the base DiscountCalculator class. 
Hence now every subclass would need to implement the discount part on itself. 
By doing this we have now removed the previous constraints that required modification to the base class. 
Now without modifying the base class we can add more apparels as well as we can change the discount amount of individual apparel as needed. 
"""