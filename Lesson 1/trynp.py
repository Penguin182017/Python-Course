import numpy as np

# 1D array
print("1D array")
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print('\n')
print(arr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print('\n')
print(arr)
print('\n')

print(" info about the array")

print(arr.ndim) # Number of dimensions (Output: 2)
print('\n')
print(arr.shape)  # Dimensions/Shape (Output: (2, 3) -> 2 rows, 3 columns)
print('\n')
print(arr.size)  # Total number of elements (Output: 6)
print('\n')
print(arr.dtype)  # Data type of elements (Output: int64 or int32)
print('\n')

print("using built-in functions")

# array of zeros
zero = np.zeros((3, 3))
print(zero)

# array of ones
ones = np.array([2, 4, 6])
print(ones)
ones = np.ones((5, 3))
print(ones)

# range of numbers

