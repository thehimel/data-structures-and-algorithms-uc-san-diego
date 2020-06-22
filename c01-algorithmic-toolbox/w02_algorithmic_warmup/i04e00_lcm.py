"""
Gind LCM of 2 given numbers.

LCM(x, y) = (x * y) / GCD(x, y)

TC: O(n)
SC: O(1)
"""


import sys


def gcd(x, y):
    while(y):
        x, y = y, x % y

    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


def test(x, y, output):
    print("Pass" if output == lcm(x, y) else "Fail")


if __name__ == "__main__":
    submit = 0

    if submit:
        input = sys.stdin.read()
        a, b = map(int, input.split())
        print(lcm(a, b))

    else:
        test(24, 60, 120)
