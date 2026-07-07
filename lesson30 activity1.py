items = ['A', 'B', 'C']
n = len(items)
total = 2 ** n

print("=== Power Map ===")
print("Items:", items)
print("Elements:", n, "   Total subsets: 2 ^", n, '=', total)
print()

print("Mask table (n =",n, "):")
mask = 0
while mask < total:
    bit2 = (mask >> 2) & 1
    bit1 = (mask >> 1) & 1
    bit0 = mask & 1
    print(" mask", mask, '-> [C][B][A] =', bit2, bit1, bit0)
    mask = mask + 1
print()
