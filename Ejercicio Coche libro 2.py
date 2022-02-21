# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 17:38:41 2022

@author: Martin
"""

class Car:
    
    def __init__(self,make,model,year):
        
        """ Iniciar atributos para describir un auto"""
        
        self.make= make
        self.model=model
        self.year= year
        self.odometer_reading= 0
        
    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name"""
        
        long_name= f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Return the mileage of the car"""
        return f"This car has {self.odometer_reading} miles on it"
    
    def update_odometer(self,mileage):
        """set the odometer reading to the given value """
        if mileage > self.odometer_reading:
            
            self.odometer_reading=mileage
            
        else:
            print("You can't roll back an odometer!")
        
    
my_new_car= Car("audi", "a4", 2019)

print(my_new_car.get_descriptive_name())
        
print(my_new_car.read_odometer())

my_new_car.update_odometer(24)

print(my_new_car.read_odometer())

my_new_car.update_odometer(25)

print(my_new_car.read_odometer())

my_new_car.update_odometer(22)

print(my_new_car.read_odometer())

