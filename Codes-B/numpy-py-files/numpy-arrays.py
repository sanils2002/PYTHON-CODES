# creating arrays
import numpy as np

arr = np.array(42)
print(arr.ndim)
print(arr)

arr = np.array([1, 2, 3, 4, 5])
print(arr.ndim)
print(arr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.ndim)
print(arr)

#index arrays
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])