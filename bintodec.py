binary = input("Enter your Binary: ")

decimal = 0
power = 0

for digit in reversed(binary):
    decimal += int(digit) * (2 ** power)
    power += 1

print("Decimal:", decimal)