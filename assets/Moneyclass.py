# Design and implement a Money class that stores monetary values in dollars and cents. Special method __init__ should have the following function header,
# def __init__(self, dollars, cents)
#Include special method __repr__ (__str__) for displaying values in dollars and cents: $ 0.45, $ 1.00, $ 1.25. Also include special method __add__, and three 
# getter methods that each provide the monetary value in another currency. Choose any three currencies to convert to.

import os
from time import sleep
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
sleep(1)
screen_clear()

class money:
    indian_cur = 75.10
    Singapur_cur = 1.35
    uk_cur = 0.73

    def __init__(self, dollers, cents=0):
        self.dollers = dollers
        self.cents = cents

    def pre(self):
        return self.dollers + (self.cents*0.01)

    def __repr__(self):
        print(f"$ {self.pre()}")

    def rupee(self):
        return (self.pre()*self.indian_cur)

    def Singapur(self):
        return (self.pre()*self.Singapur_cur)

    def UK(self):
        return (self.pre()*self.uk_cur)


m = money(10)
m.__repr__()
print(f"{m.rupee()}")
print(f"{m.Singapur()}")
print(f"{m.UK()}")
