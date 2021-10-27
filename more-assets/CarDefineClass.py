# Define a class Car having variables as speed and gear. Its __init__() method should take self, speed and gear as arguments. Make sure to set these appropriately in the body of the __init__() method.
# It should have 2 methods:
# i) void changeGear(newValue) – Changes gear and returns gear.
# ii) void speedUp(incrementFactor) – Increases the speed and returns speed.
# Note: Do not create any objects of the class and do not call any method.

# You should create a class named Car with 2 instances variables. 
# Write _init_() method in the class with self, speed and gear as arguments. 
# Wrtie the 3 functions given below inside the class.
# Do not create any object of the class.

# INITIALLY THIS CODE CONTAINS ERROR AS CLASS IS NOT CREATED.
# ONCE YOU CREATE CLASS AND PUT THESE FUNCTIONS INSIDE THE CLASS, THE CODE WOULD NOT CONTAIN ERROR.

class Car:
    def _init_(self, speed, gear):
        # initialize the variable here
        self.speed=speed
        self.gear=gear
        
    def changeGear(self, newValue):
        # Write the body of the function
        self.gear=newValue
        return self.gear

    def speedUp(self, incrementFactor):
        # Write the body of the function
        self.speed +=incrementFactor
        return self.speed
