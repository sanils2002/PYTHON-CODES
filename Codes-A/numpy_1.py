import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5, 6])
c = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# print(a)
# print(b[0])
# print('2nd element on 1st row: ', c[0, 1])
# print('Last element from 2nd dim: ', c[1, -1])
# print(d[0, 1, 2])

#Slicing in python means taking elements from one given index to another given index.
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].

# print(b[1:3])
# print(b[3:])
# print(b[:3])
# print(b[-3:-1])   # b = [1, 2, 3,4,5,6]
# print(b[1:4:2])
# print(b[::2])
# print(c[1, 1:4])  #c = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
# print(c[0:2, 2])

# # Data Type
# print(a.dtype)
# print(b.dtype)

# Array Shape
# print(c.shape)
# print(d.shape)

# # Reshape

# e = b.reshape(2, 3)
# print(e)

# Fetching elements in loop
# for x in b:
#   print(x)

# for x in c:
#   print(x)

# for x in c:
#     for y in x:
#         print(y)

# Join Array
# b1 = np.array([7, 8, 9, 10])
# print(b1)

# bb1 = np.concatenate((b,b1))
# print(bb1)

# c1 = np.array([[13, 14, 15], [16, 17, 18]])
# cc1 = np.concatenate((c,c1), axis=1)
# print(cc1)

# cc2 = np.concatenate((c,c1), axis=1)
# print(cc2)

# # Split Array
# new_b = np.array_split(b, 2)
# print(new_b)

# print(new_b[0])
# print(new_b[1])

# # # Search in an array

# x = np.where(b == 4)
# print(x)

# # # Sort an Array
# s=np.array([27, 34, 11, 3])
# print(np.sort(s))

