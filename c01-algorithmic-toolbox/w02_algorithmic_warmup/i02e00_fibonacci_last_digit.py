"""
Calculate n fibonacci numbers. and return it's last digit.

TC: O(1)
SC: O(1)
"""

import sys


def fib(n):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** n + 1) / 5 ** 0.5)


def fib_last(n):
    fib_num = fib(n)
    last_digit = fib_num % 10
    return last_digit


def test(input, output):
    print("Pass" if output == fib_last(input) else "Fail")


if __name__ == "__main__":
    submit = 0

    if submit:
        input = sys.stdin.read()
        n = int(input)
        print(fib_last(n))

    else:
        test(1, 1)
        test(2, 1)
        test(3, 2)
        test(12, 4)
        test(30, 0)
        test(300, 4)
