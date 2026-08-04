arr = [1, 3, 5, 2, 2]
print("Full array: ", arr)

index = 2
left_sum = sum(arr[:index])
right_sum = sum(arr[index + 1:])

print("Left sum:", left_sum)
print("Right sum:", right_sum)

for i in range(len(arr)):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i + 1:])
    print("Index", i, "-> Left sum:", left_sum, "Right sum:", right_sum)

    if left_sum == right_sum:
        print("Equilibrium point found at index", i)

for i in range(1, len(arr)):
    window = arr[:1]
    print("Window: ", window, "sum: ", sum(window))

target = 5
for i in range(len(arr)):
    for j in range(i + 1, len(arr) + 1):
        subarray = arr[i:j]
        if sum(subarray) == target:
            print("target sum found subarray in subarray target sum: ", subarray)
            
