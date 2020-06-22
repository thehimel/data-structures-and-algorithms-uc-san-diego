"""
Calculate n fibonacci numbers.

Input: 2
Output: 1

Input: 10
Output: 55

Solution: https://leetcode.com/problems/fibonacci-number/solution/

TC: O(1)
SC: O(1)
"""


def fib(n):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** n + 1) / 5 ** 0.5)


def test(input, output):
    print("Pass" if output == fib(input) else "Fail")


if __name__ == "__main__":
    submit = 0

    if submit:
        n = int(input())
        print(fib(n))

    else:
        test(1, 1)
        test(2, 1)
        test(3, 2)
        test(12, 144)
        test(30, 832040)
