class MyClass: # defining class
    __a = 0;
    def sum(self, increment):
        self.__a += increment
        print(self.__a)
b = MyClass() # creating instance of class
b.sum(2)
b.sum(5)
print(b.__a)