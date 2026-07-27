scores = [10, 20, 30, 40, 50]
start, end = 0, len(scores) - 1
while start < end:
    scores[start], scores[end] = scores[end], scores[start]
    start += 1
    end -= 1
print("Swapped: ", scores)
print()

scores = [1, 2, 3, 4, 5,6 , 7, 8]
n, i = 3, 0
while i < len(scores):
    start, end = i, min(i + n - 1, len(scores) - 1)
    while start < end:
        scores[start], scores[end] = scores[end], scores[start]
        start += 1
        end -= 1
    i += n
print("Reversed in groups of 3:", scores)
print()

scores = [10, 20, 30, 40, 50]
for _ in range(2):
    temp = scores[0]
    for i in range(1, len(scores)):
        scores[i - 1] = scores[i]
    scores[-1] = temp
print("Rotated left by 2:", scores)
print()

scores = [16, 17, 4, 3, 5, 2]
max_right = scores[-1]
leaders = [max_right]
for i in range(len(scores) - 2, -1, -1):
    if scores[i] > max_right:
        max_right = scores[i]
        leaders.append(scores[i])
leaders.reverse()
print("Scores:", scores)
print("Leaders:", leaders)

