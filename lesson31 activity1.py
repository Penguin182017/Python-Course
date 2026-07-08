print("=== Dream Recursion Lab ===")
print("Two rules of recursion:")
print("   1. call yourself with a smaller problem each time")
print("   2. have a base case that stops the calls")
print()

def count_up(n):
    if n > 10:
        return
    print(n, end=' ')
    count_up(n + 1)

print("counting up from 1 to 10 using recursion:")
count_up(1)
print()
print()

def countdown(n):
    if n == 0:
        print("Liftoff!")
        return
    print(n, end=' ')
    countdown(n-1)

print("countdown (builds down, unwinds up):")
countdown(5)
print()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("factorial using recursion:" )
print("factorial(5)", factorial(5))
print("factorial(4)", factorial(4))
print("factorial(1)", factorial(1))
print("factorial(0)", factorial(0))
print()

import sys
print("python recursion limit:", sys.getrecursionlimit(), "calls")

def no_base_case(n):
    print("call", n, end=" ")
    no_base_case(n + 1)

sys.setrecursionlimit(30)
try:
    no_base_case(1)
except RecursionError:
    print("RecursionError! Stack overflow -- no base case!")

sys.setrecursionlimit(1000)
print("Rule: always include a base case in every recursive function!")