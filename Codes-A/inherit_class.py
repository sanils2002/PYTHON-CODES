class Person:
    "This is the Base Class"
    def get_name(self, name):
        "This is the Person Class Function"
        self.name= name
    def get_details(self):
        return self.name

class Student(Person):
    def fill_details(self, name, branch, year):
        Person.get_name(self, name)
        self.branch = branch
        self.year = year
    def get_details(self):
        print("Name:", Person.get_details(self))
        # print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)

p1=Person()
s1=Student()

p1.get_name("ABC")
s1.fill_details("XYZ", "CSE", 2020)

print(p1.get_details())
s1.get_details()

# Class built-in Attributes

print(Student.__bases__)
print(Student.__dict__)
print(s1.__dict__)
print(Student.__name__)
print(s1.__module__)
print(Person.__doc__)
print(Person.get_name.__doc__)
print(p1.get_name.__doc__)
