# Create a class called Triangle with 3 instances variables that represents 3 angles of triangle. Its __init__() method should take self, angle1, angle2, and angle3 as
# arguments. Make sure to set these appropriately in the body of the __init__() method. Create a method named check_angles(self). It should return True if the sum of the three
# angles is equal to 180, and False otherwise.
# Note: Do not create any objects of the class and do not call any method.

class Triangle:
 def _init_(self, angle1,angle2, angle3):
    self.angle1=angle1
    self.angle2=angle2
    self.angle3=angle3

    # initialize the 3 angles in this method

 def check_angles(self):
  if self.angle1+self.angle2+self.angle3 ==180:
    return True
  else:
    return False
