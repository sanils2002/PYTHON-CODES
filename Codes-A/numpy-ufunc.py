# ufuncs : "Universal Functions"
# NumPy functions that operates on the ndarray object.

# Example: Add the Elements of Two Lists
# list 1: [1, 2, 3, 4]    list 2: [4, 5, 6, 7]

# Approach 1: iterate over both of the lists and then sum each elements
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

# Approach 2: with numpy ufunc called add(x, y)
import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)