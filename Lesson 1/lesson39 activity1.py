binary = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
streak = 0
for num in binary:
    if num == 0:
        streak = 0
    else:
        streak += 1
    print(num, '->', streak)
print()

streak = 0
best = 0
for num in binary:
    if num == 0:
        streak = 0
    else:
        streak += 1
        if streak > best:
            best = streak
print("Binary array: ", binary)
print("max consecutive: ", best)
print()

nums = [1, 0, 3, 6, 0, 0, 0, 2, 335, 0, 72]
print("before: ", nums)
zero = 0
for nonzero in range(len(nums)):
    if nums[nonzero] != 0:
        nums[nonzero], nums[zero] = nums[zero], nums[nonzero]
        zero += 1
print("After: ", nums)
print()

print("Write pointer stopped at: ", zero)
print("Non-zeros at front:       ", zero)
print("zeros at the end:         ", len(nums) - zero)