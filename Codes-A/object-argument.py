class Triangle:
	pass

t1 = Triangle()
t1.a = 10
t1.b = 18
t1.c = 23

def perimeter(obj):
	per = obj.a + obj.b + obj.c
	print("Perimeter of triangle: ", per)

# Passing object as argument	
perimeter(t1)