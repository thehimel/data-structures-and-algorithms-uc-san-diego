import sys


def get_fibonacci_last_digit_naive(n):
    golden_ratio = (1 + 5 ** 0.5) / 2
    fib_num = int((golden_ratio ** n + 1) / 5 ** 0.5)
    last_digit = fib_num % 10
    return last_digit


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
