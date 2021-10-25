#Write a program to calculate area of square and rectangle. Use method overloading for this, that is, define a method area() which can take one parameter or two
#parameter. If area is called with one parameter, then it will calculate area of square and with two parameters then it will calculate area of rectangle.

import os
from time import sleep
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
sleep(1)
screen_clear()

class Compute:
   def area(self, x=None, y=None):
      if x!=None and y !=None:
         return x*y
      elif x!=None:    
         return x*x
      else:
         return 0  

obj = Compute()
print(obj.area())
print(obj.area(6))
print(obj.area(2,8))
