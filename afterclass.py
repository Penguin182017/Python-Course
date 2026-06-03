def Myfunction1(n):
    if n <= 0:
        return 0
    return n + Myfunction1(n//2) + Myfunction1(n//3)

def Myfunction2(n):
    if n <= 1:
        return 0
    return 1 + Myfunction2(n-1)

print("Myfunction1(6) =", Myfunction1(6))
print("Myfunction2(6) =", Myfunction2(6))