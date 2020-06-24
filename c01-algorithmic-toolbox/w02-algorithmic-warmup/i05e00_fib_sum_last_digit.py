"""
Problem Statement:
Retun the last digit of the sum o n fibonacci numbers. In other words,
Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
Constraints. 0 ≤ 𝑛 ≤ 107.

Example:
Input: 3
Output: 4
𝐹0 + 𝐹1 + 𝐹2 + 𝐹3 = 0 + 1 + 1 + 2 = 4.

Solution: We just need to add the last digits of all fibonacci numbers than
return the last digit.


Similar Problem Statement:
Return the last digit of n fibonacci numbers. Constraints. 0 ≤ 𝑛 ≤ 107.

Input: 3
Output: 2
𝐹3 = 2

Input: 331
Output: 9
𝐹331 = 668 996 615 388 005 031 531 000 081 241 745
    415 306 766 517 246 774 551 964 595 292 186 469.

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


def fib_sum_last(n):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += fib_last(i)

    return total_sum % 10


def test(input, output):
    print("Pass" if output == fib_sum_last(input) else "Fail")


if __name__ == "__main__":
    submit = 0

    if submit:
        input = sys.stdin.read()
        n = int(input)
        print(fib_sum_last(n))

    else:
        test(3, 4)
        test(100, 5)
