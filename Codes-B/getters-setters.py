class A:
    def __init__(self,p):
        self.__p = p #Defining private member
    def getP(self): #Defining getters
        return self.__p
    def setP(self, p): #Defining Setters
        self.__p = p
a1 = A(22)
print(a1.getP()) #Getting value through get function
a1.setP(43) #Setting value through set function
print(a1.getP())