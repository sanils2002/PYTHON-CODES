class Parent:
	def ovr_method(self):
		print('This is in Parent Class')
class Child(Parent):
	def ovr_method(self):
		print('This is in Child Class')
c = Child()
c.ovr_method()