"""
Calculate n fibonacci numbers.

Input: 2
Output: 1

Input: 10
Output: 55

"""


def fib(n):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** n + 1) / 5 ** 0.5)


n = int(input())
print(fib(n))
