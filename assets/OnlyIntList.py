import os
from time import sleep
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
sleep(1)
screen_clear()

class AvgList(list):
  def avg(self):
     for items in self:
        if not isinstance(items,int):
            raise ValueError('Invalid item in list. All items need to be an integer.')

     return sum(self)/len(self)

mylist = AvgList()

mylist.append(1)
mylist.append(5)
mylist.append(10)

print(mylist)
print(mylist.avg())
