"""
Given 2 digits, return the sum of them.

Input: 2 5
Output: 7
"""


def get_sum(x, y):
    return x + y


def test(x, y):
    ans = x + y
    print("Pass" if ans == get_sum(x, y) else "Fail")


if __name__ == '__main__':
    submit = 0

    if submit == 1:
        x, y = map(int, input().split())
        print(get_sum(x, y))

    else:
        test(2, 3)
