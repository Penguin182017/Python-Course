binary_scores = [1, 0, 1, 1, 1, 0, 0, 1]
print("Before: ", binary_scores)
current_streak = 0
best_streak = 0
for num in binary_scores:
    if num == 1:
        current_streak += 1
        if current_streak > best_streak:
            best_streak = current_streak

    else:
        current_streak = 0

print("longest streak: ", best_streak)   

arr = [2, 0, 4, 33, 0, 7]
write_pointer = 0
for read_pointer in range(len(arr)):
    if arr[read_pointer] != 0:
        arr[write_pointer] = arr[read_pointer]
        write_pointer += 1

for i in range(write_pointer, len(arr)):
    arr[i] = 0
print(arr)

