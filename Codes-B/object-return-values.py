#from _typeshed import Self

class Triangle:
    def create_triangle(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        print("The triangle is created")
    def print_sides(self):
        print('Side a: ', self.a)
        print('Side b: ', self.b)
        print('Side c: ', self.c)

t1 = Triangle()
t1.create_triangle(10,20,30)

def size_double(obj):
	t2 = Triangle()
	t2.a = t1.a *2
	t2.b = t1.b *2
	t2.c = t1.c *2
    # Returning object
	return t2 
# Passing object as argument    
t2 = size_double(t1) 
t2.print_sides()