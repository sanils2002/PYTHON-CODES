# shuffle() and permutation()
from numpy import random
import numpy as np

# shuffle() method changes the original array.
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

# Generate a random permutation
# permutation() method returns a re-arranged array 
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
print(arr)