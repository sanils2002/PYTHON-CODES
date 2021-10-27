# Create a class called Die with one integer instance variable called sideUp. Its __init__() method should take self, sideUp as arguments. Make sure to set these appropriately in
# the body of the __init__() method. The class should have two methods: 1) getSideUp() and roll( ).
# a. getSideUp() – Should return the side up.
# b. roll() – Should set sideUp to a new value and returns the side up.
# Note: Do not create any objects of the class and do not call any method.

import random

class Die():
    def _init_(self, sideUp):
        # initialize the variable here
        self.sideUp = sideUp

    def getSideUp(self):
        # Write the body of the function
        return self.sideUp

    def roll(self):
        # Write the body of the function
        self.sideUp = random.randint(1, 6)
        return self.sideUp
