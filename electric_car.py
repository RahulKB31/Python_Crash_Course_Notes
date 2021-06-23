"""A set of classes that can be used to represent electric cars."""

from car_1 import Car

class Battery():
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=60):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
        
    def get_range(self):
        """Print a statement about the range this batter provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
        
class ElectricCar(Car):
    """Model aspects of a car, specific to electric vehicles."""
     
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class. Then initialize attributes"""
        super().__init__(make, model, year)
        self.battery = Battery()
        