import numpy as np

a = np.arange(9, dtype=np.float64).reshape(3, 3)
print('first array:')
print(a)
print('\n')

b = np.array([10, 10, 10])
print('second array:')
print(b)
print("\n")

print("add the two arrays")
print(np.add(a, b))
print('\n')

print("subtract the two arrays")
print(np.subtract(a, b))
print('\n')

print("multiply the two arrays")
print(np.multiply(a, b))
print('\n')
