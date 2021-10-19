class MyClass(object): # Defining class
    def __init__(self, x, y, z):
        self.var1 = x # public data member
        self._var2 = y # protected data member
        self.__var3 = z # private data member
obj = MyClass(3,4,5)
print(obj.var1)
obj.var1 = 10
print(obj.var1)
print(obj._var2)
obj._var2 = 12
print(obj._var2)
#obj.__var3