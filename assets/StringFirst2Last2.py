import os
from time import sleep
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
sleep(1)
screen_clear()

def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

s1=input("Enter String 1:")
s2=input("Enter String 2:")
s3=input("Enter String 3:")

screen_clear()

print(string_both_ends(s1))
print(string_both_ends(s2))
print(string_both_ends(s3))
