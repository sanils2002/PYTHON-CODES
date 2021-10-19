import os
from time import sleep
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
sleep(1)
screen_clear()

x=int(input("Enter Lower Limit:"))
y=int(input("Enter Upper Limit:"))

screen_clear()

items = []
for i in range(x, y+1):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
print( ",".join(items))
