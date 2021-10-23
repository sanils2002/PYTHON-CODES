import os
from time import sleep
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
sleep(1)
screen_clear()

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Enter the number:"))

screen_clear()

print_factors(num)
