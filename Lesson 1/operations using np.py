import numpy as n

arr = n.arange(0, 10)
print("original arrary: ", arr)

new_arr  = arr.copy()
new_arr[new_arr % 2 != 0] = -1

print("modified array (odds replaced):", new_arr)
print("original still unchanged: ", arr)

td = arr.reshape(2, 5)
print("2D array:\n", td)

even_sum = 0

for num in arr:
    if num % 2 == 0:
        even_sum += num

print("Sum of even numbers:", even_sum)

