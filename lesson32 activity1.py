def linear(n):
    if n == 0:
        return
    print(n, end=' ')
    linear(n - 1)

print("Linear recursion (one call per level):")
linear(5)
print()

def tail(n):
    if n == 0:
        return
    print(n, end=' ')
    tail(n - 1)

print("Tail recursion (prints going down):")
tail(5)
print()

def head(n):
    if n == 0:
        return
    head(n - 1)
    print(n, end=' ')

print("Head recursion (prints coming up):")
head(5)
print()

def inc_dec(n):
    if n == 0:
        return
    print(n, end=' ')
    inc_dec(n - 1)
    print(n, end=' ')

print("Increasing-Decreasing (down then up):")
inc_dec(5)
print()

def tree(n):
    if n == 0:
        return
    print(n, end=' ')
    tree(n - 1)
    tree(n - 1)

print("Tree recursion (two calls -- branches double):")
tree(3)
print()
print("Level calls: 1 -> 2 -> 4 -> 8 (doubles every level!)")