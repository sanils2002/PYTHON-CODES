import os
from time import sleep
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
sleep(1)
screen_clear()

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))
