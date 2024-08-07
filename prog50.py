#  Write a Python program to create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f" name of vehicle = {self.name} \n Max Speed = {self.max_speed} \n Mileage of vehicle  = {self.mileage} "

my_car = Vehicle("Toyota fortuner", 150, 30000)
my_car = Vehicle("Toyota fortuner", 150, 30000)
print(my_car)
print(my_car)