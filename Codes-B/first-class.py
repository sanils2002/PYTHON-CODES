class Student:
	'student details'
	def fill_details(self,name,branch,year):
		self.name = name
		self.branch = branch
		self.year = year
		print("A Student detail object is created")
	def print_details(self):
		print("Name: ", self.name)
		print("Branch: ",self.branch)
		print("Year: ",self.year)

# creating an object of Student class
s1 = Student()
# creating another object of Student class
s2 = Student()

# using the method fill_details with proper attributes
s1.fill_details('John','CSE','2002')
s2.fill_details('Jack','ECE','2004')

# using the print_detail method with proper attributes
s1.print_details()
s2.print_details()

# Example of mutate objects
# Create an instance of class Student
s1 = Student()
# Fill details in that object
s1.fill_details('John','ECE',2004)

# Printing details of the mutated object s1
s1.print_details()