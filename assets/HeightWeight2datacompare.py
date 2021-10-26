import os
from time import sleep
def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')
sleep(1)
screen_clear()

class student():
    def getinfo(self,height,weight):
        self.height=height
        self.weight=weight
    def printinfo(self):
        print("Height (in cm): ",self.height)
        print("Weight (in kg): ",self.weight)
        print("\n")
def compare(obj1,obj2):
    if obj1.height > obj2.height:
        print("Student 1 is heighted than Student 2")
    else:
        print("Student 2 is heighted than Student 1")
    if obj1.weight > obj2.weight:
        print("Student 1 is heavier than Student 2")
    else:
        print("Student 2 is heavier than Student 1")
s1=student()
s2=student()
s1.getinfo(12,45)
s1.printinfo()
s2.getinfo(15,47)
s2.printinfo()
compare(s1,s2)
