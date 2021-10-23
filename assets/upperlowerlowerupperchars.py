# write a function biggest, which returns the key corresponding to the entry with the largest 
# number of values associated with it. If there is more than one such entry, return any one of the matching keys.

import os
from time import sleep
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
sleep(1)
screen_clear()

with open('D:/IIIT Nagpur/2nd Year/3rd Semester/IT-Workshop 1/test.txt', 'r') as inp:
    y = inp.read().swapcase()
with open('D:/IIIT Nagpur/2nd Year/3rd Semester/IT-Workshop 1/write.txt', 'a') as out:
    out.write(y)
