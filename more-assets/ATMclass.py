# An ATM contains Indian currency notes of 100, 500 and 2000. To withdraw cash from this ATM, the user has to enter the amount. The ATM then calculates the number of
# notes of each currency, i.e. of 100, 500 and 2000. Write a function findDenom(amount) that returns dictionary containing mapping of currency and its number of notes.

def findDenom(amount):
    dict1={}
    a = 0
    b = 0
    c = 0


    if(amount >=2000 ):
        a = (int)(amount / 2000)
        amount = amount - a*2000
    if(amount>=500):
        b = (int)(amount/500)
        amount = amount - b*500
    if(amount>=100):
        c = (int)(amount / 100)
        amount = amount - a*100

    dict1 = {2000:a , 500:b , 100:c}
        
    
    # write function body
    return dict1

#dict2 = findDenom(3300)
#print(dict2)
