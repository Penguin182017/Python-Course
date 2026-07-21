keypad = {
    "2": ["a", 'b', 'c'],
    "3": ["d", 'e', 'f'],
    "4": ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']

}

def combinations(digits, current):
    if len(digits) == 0:
        print(current)
        return
    
    first_digit = digits[0]
    remaining = digits[1:]

    for letter in keypad[first_digit]:
        combinations(remaining, current + letter)

number = input("enter digits (e.g. 23): ")
print("All combinations:")
combinations(number, "")

count = 1
for digit in number:
    count = count * len(keypad[digit])
print("Total combinations:", count)