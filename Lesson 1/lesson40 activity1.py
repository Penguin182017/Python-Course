nums = [2, -5, 3, 4, -1, 6, -3]
print("Full array: ", nums)
print()
print("Some Subarrays")
print("  [0:2] = ", nums[0:2], " sum = ", sum(nums[0:2]))
print("  [2:6] = ", nums[2:6], " sum = ", sum(nums[2:6]))
print("  [3:7] = ", nums[3:7], " sum = ", sum(nums[3:7]))
print()

print("Running sum trace:")
running = 0
for num in nums:
    running += num
    if running < 0:
        print(f"  {num} -> sum = {running} <-- negative! RESET to 0")
        running = 0
    else:
        print(f"  {num} -> sum = {running}")
print()

running = 0
best = 0
for num in nums:
    running += num
    if running < 0:
        running = 0
        if running > best:
            best = running
print("Array: ", nums)
print("Max subarray sum: ", best)
print()

hard = [1, 2, 3, -4, 5, -22, -4, 25, 2, -9]
running = 0
best = 0
for num in hard:
    running += num
    if running < 0:
        running = 0
    if running > best:
        best = running
print("Array: ", hard)
print("Max subarry sum: ", best)