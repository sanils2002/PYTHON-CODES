# generate random numbers
from numpy import random

# random integer
x = random.randint(100)
print(x)

# random float between 0 to 1
x = random.rand()
print(x)

# Generate a 2-D array containing 3 rows and 5 random integers
x = random.randint(100, size=(3, 5))
print(x)

# 1-D array with 5 random floats:
x = random.rand(5)
print(x)

# Generate Random Number From Array
x = random.choice([3, 5, 7, 9])
print(x)

# Random Data Distribution
# 2-D array with 3 rows, each containing 5 values.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))