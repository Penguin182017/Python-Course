def multiply_once(a, b):
    return a * b


def multiply_n_times(a, b):
    total = 0
    negative = (a < 0) ^ (b < 0)
    a_abs = abs(a)
    b_abs = abs(int(b))

    for _ in range(b_abs):
        total += a_abs

    if negative:
        total = -total

    return total


def main():
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))

    print('Result using direct multiply:', multiply_once(x, y))
    print('Result using repeated addition:', multiply_n_times(x, y))


if __name__ == '__main__':
    main()
