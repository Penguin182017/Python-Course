n = 12

print("=== Power Surge ===")
print("n       =", n, "->", bin(n))
print("n - 1   =", n - 1, '->', bin(n -1))
print('n&(n-1) =', n & (n - 1), '->', bin(n & (n - 1)))

print("Power of 2 Check: ")
for x in [1, 4, 6, 16, 18, 64]:
    result = x > 0 and (x & (x - 1)) == 0
    print('', x, '->', bin(x), '->', result)

    def pow4(n):
        if n <= 0 or n & (n - 1) != 0:
            return False
        count = 0
        while n > 1:
            n = n >> 1
            count = count + 1
        return count % 2 == 0
    
print(" Power of 4 check:")
for x in [1, 4, 8, 16, 32, 64]:
    print(' ', x, '->', pow4(x))
    
def pow8(n):
    if n <= 0 or n & (n - 1) != 0:
        return False
    count = 0
    while n > 1:
        n = n >> 1
        count = count + 1
    return count % 3 == 0

print('Power of 8 check:')
for x in [1, 8, 16, 64, 32, 512]:
    print(' ', x, '->', pow8(x))