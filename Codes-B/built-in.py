# Create the class Student
class Student:
    'student details'
# Add method member fill_details
    def fill_details(self,name,branch,year):
        self.name = name
        self.branch = branch
        self.year = year
        print("A Student detail object is created")
# Add method member print_details
    def print_details(self):
        print('Name: ', self.name)
        print('Branch: ',self.branch)
        print('Year: ',self.year)
print("Student.__doc__: ",Student.__doc__)
print("Student.__name__: ",Student.__name__)
print("Student.__module__: ",Student.__module__)
print("Student.__bases__: ",Student.__bases__)
print("Student.__dict__: ", Student.__dict__)