# Write a program to define a class Bank that keeps track of bank customers. The class should contain the following data members:
# Name - Customer Name
# accNumber - Account Number
# accType - Account Type (Saving/Current)
# Amount - Amount deposited in the bank account
# Interest - Interest earned by the customer
# The class should support the following methods:
# __init__() for initialization of the data members
# deposit() for depositing the money in the account
# Withdrawal() for withdrawing money from account
# __str__() for displaying the information about the bank customer
# findInterest() that determines the interest on the basis of amount in the account as below:
# a. >=5,00,000 8% interest per annum
# b. >=3,00,000 and < 5,00,000 7% interest per annum
# c. >=1,00,000 and <3,00,000 5% interest per annum
# d. <1,00,000 3% interest per annum

import os
from time import sleep
def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')
sleep(1)
screen_clear()

class Bank:

    def findinterest(self):
        a = self.amount
        if a >= 500000:
            self.interest = 8
        elif a >= 300000 and a < 500000:
            self.interest = 7
        elif a >= 100000 and a < 300000:
            self.interest = 5
        elif a < 100000:
            self.interest = 3

    def __init__(self, name, Number, Type, amount):
        self.name = name
        self.Number = Number
        self.Type = Type
        self.amount = amount
        self.interest = 0
        self.findinterest()

    def deposite(self, money):
        self.amount = self.amount + money
        self.findinterest()

    def withdrawl(self, money):
        self.amount = self.amount - money
        self.findinterest()

    def __str__(self):
        return ('Name : ' + self.name + '\nAccount Number : ' + self.Number + '\nAccount type : '+self.Type + '\nAmount : '+str(self.amount)+'\nInterest : '+str(self.interest)+'%')


B = Bank('Sanil', '123456789', 'Saving', 20000)

rep = B.__str__()
print(rep)
B.deposite(300000)

print("\n")

rep = B.__str__()
print(rep)
