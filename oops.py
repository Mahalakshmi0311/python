class Car:
    # Constructor method
    def __init__(self, brand, speed):
        self.brand = brand          # Public attribute
        self.__speed = speed        # Private attribute (encapsulation)

    def accelerate(self, increment):
        self.__speed += increment
        return f"{self.brand} speed is now {self.__speed} km/h"

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, speed, battery_size):
        super().__init__(brand, speed)
        self.battery_size = battery_size

    def describe(self):
        return f"{self.brand} has a {self.battery_size}kWh battery."

# Usage
my_ev = ElectricCar("Tesla", 120, 75)
print(my_ev.accelerate(15))
print(my_ev.describe())
