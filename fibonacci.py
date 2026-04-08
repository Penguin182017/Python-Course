def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence


def main():
    terms = int(input("How many terms: "))

    if terms <= 0:
        print("Please enter a positive number.")
        return

    result = fibonacci(terms)
    print(f"Fibonacci sequence with {terms} term(s):")
    print(result)


main()
