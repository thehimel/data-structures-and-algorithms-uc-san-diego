"""
Return the last digit of n fibonacci numbers.

Solution:
https://medium.com/competitive/the-last-digit-of-a-large-fibonacci-number-ea3b12da58bc

Instead of storing the whole Fibonacci number,
just store their modulus and calculate the next one using that.

TC: O(n)
SC: O(1)
"""

import sys


def fib_last(n):
    if n <= 1:
        return 1

    first = 0
    second = 1

    res = None

    # for (i=2; i<=n; i++)
    for i in range(2, n+1):
        res = (first + second) % 10
        first, second = second, res

    return res


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
        test(331, 9)
        test(327305, 5)
