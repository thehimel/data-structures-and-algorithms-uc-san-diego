"""
Given an array of integers. Return the max product possible by
multiplying 2 numbers from that array.

Solution:
Find the max 2 numbers in the array.
With one for loop, find the first number. And with another for loop,
find the second number. While finding the second number, make sure you
skip the index of the first number.

TC: O(n)
SC: O(1)

Input:
10
0 1 2 3 4 5 6 7 8 9

Line1: Number count
Line2: Array of numbers

Output:
72

Input:
10
10 20 30 80 5 9 90 5 2 1

Output:
7200
"""


def max_pairwise_product(numbers):

    first_index = None
    second_index = None

    for index, num in enumerate(numbers):
        if first_index is None:
            first_index = index

        elif num > numbers[first_index]:
            first_index = index

    for index, num in enumerate(numbers):
        if index == first_index:
            continue

        if second_index is None:
            second_index = index

        elif num > numbers[second_index]:
            second_index = index

    max_product = numbers[first_index] * numbers[second_index]
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
