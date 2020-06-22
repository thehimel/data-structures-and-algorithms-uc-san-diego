"""
Gind GCD of 2 given numbers.

Solution: https://www.youtube.com/watch?v=JYn-XG-d7AA

TC: O(n)
SC: O(1)
"""

import sys


def gcd(x, y):
    while(y):
        x, y = y, x % y

    return x


def test(x, y, output):
    print("Pass" if output == gcd(x, y) else "Fail")


if __name__ == "__main__":
    submit = 0

    if submit:
        input = sys.stdin.read()
        a, b = map(int, input.split())
        print(gcd(a, b))

    else:
        test(12, 8, 4)
        test(8, 12, 4)
        test(234, 357, 3)
        test(357, 234, 3)
