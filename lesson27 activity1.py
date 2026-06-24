a,b = 7, 7

print("=== Odd Hunt ===")
print("a ^ a = ", a ^ a)
print("a ^ 0 = ", a ^ 0)
print("Equal (XOR):", (a ^ b) == 0)
print()

arr = [3, 5, 3, 5, 9]
result = 0
for n in arr: result ^= n
print("XOR of", arr, "=", result)
print()

nums = [4, 7, 4, 2, 7, 2, 9]
res = 0
for n in nums: res ^= n
print("Odd occuring:", res)
print()

pair = [3, 9, 3, 5, 5, 7]
xab = 0
for n in pair: xab ^= n
print("XOR of two odds;", xab, "->", bin(xab))
print()

setbit = xab & -xab
x, y = 0, 0
for n in pair:
    if n & setbit: x ^= n
    else: y ^= n
print("Two odd-occurring:", x, "and", y)

