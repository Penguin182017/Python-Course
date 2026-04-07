num = int(input("Enter a number: "))

n = num
sum = 0
digits = str(num)
count = len(digits)

for i in range(count):
    digit = n % 10
    sum += digit ** count
    n = n // 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")