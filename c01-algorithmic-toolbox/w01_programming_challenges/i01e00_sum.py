"""
Given 2 digits, return the sum of them.

Input: 2 5
Output: 7
"""


def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
