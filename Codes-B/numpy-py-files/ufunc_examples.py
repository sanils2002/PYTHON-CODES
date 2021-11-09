import numpy as np

l1 = np.array([4, 1, 9, 3])
l2 = np.array([1, 6, 3, 0])

#-------------------------------------------------------------

# Rounding Decimals
# There are primarily five ways of rounding off decimals in NumPy:

# # truncation
# arr = np.trunc([76.6754, -13.435])
# print(arr)

# # fix
# arr = np.fix([76.6754, -13.435])
# print(arr)

# # rounding
# arr = np.around(76.6754)
# print(arr)

# arr = np.around(76.6754, 2)
# print(arr)

# # floor
# arr = np.floor([76.265, -13.435])
# print(arr)

# # ceil
# arr = np.ceil([76.265, -13.435])
# print(arr)

#-------------------------------------------------------------
# LOGS

arr = np.arange(1, 10)
print(arr)
print(np.log2(arr))
print(np.log10(arr))
print(np.log(arr))  # log to the base e
#-------------------------------------------------------------

# Addition is done between two arguments whereas summation happens over n elements.
# Summations
a1 = np.sum([l1,l2])
print(a1)

# NumPy will sum the numbers in each array.
a2 = np.sum([l1,l2], axis = 1)
print(a2)

# cummulative summation
a3 = np.cumsum(l1)
print(a3)

# Products
a1 = np.prod([l1,l2])
print(a1)

# NumPy will return the product of each array.
a2 = np.prod([l1,l2], axis = 1)
print(a2)

# cummulative product
a3 = np.cumprod(l1)
print(a3)

#Difference

# subtracting two successive elements.
a1 = np.diff(l1)
print(a1)

# Compute discrete difference of the following array twice
a2 = np.diff(l1, n=2)
print(a2)

# Set Operations

a1 = np.array([2,3,5,2,1,2,3,1,5,5,3])

b = np.unique(a1)
print(b)

a2 = np.union1d(l1,l2)
print(a2)

a3 = np.intersect1d(l1,l2)
print(a3)

a4= np.setdiff1d(l1,l2)
a5= np.setdiff1d(l2,l1)
print(a5)
print(a4)

# LCM
a1 = np.lcm.reduce(l1)
print(a1)
arr = np.array([[3, 6, 9], [2,3,5]])
a2 = np.lcm.reduce(arr)
print(a2)

# GCD
a1 = np.gcd.reduce(l1)
print(a1)
arr = np.array([[3, 6, 9], [2,3,5]])
a2 = np.gcd.reduce(arr)
print(a2)