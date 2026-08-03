print("=" * 40)
print("       ARRAY ENERGY TRACKER")
print("=" * 40)

nums = [4, -2, -7, 1, -3, 5, -1, 2]
print("Array: ", nums)
print()
print("Some Subarrays")
print("[0:2] = ", nums[0:2], " sum = ", sum(nums[0:2]))
print("[2:6] = ", nums[2:6], " sum = ", sum(nums[2:6]))
print("[3:8] = ", nums[3:8], " sum = ", sum(nums[3:8]))


def max_subarray_sum(nums):

    running = 0
    max_so_far = nums[0]

    for num in nums:
        running += num
        print("Added", num, "-> running sum is: ",running)

        if running > max_so_far:
            max_so_far = running

        if running < 0:
            print("Running sum is negative, reset to 0")
            running = 0

    return max_so_far