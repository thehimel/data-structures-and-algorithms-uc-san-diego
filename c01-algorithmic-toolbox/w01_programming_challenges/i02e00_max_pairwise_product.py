"""
Given an array of integers. Return the max product possible by
multiplying 2 numbers from that array.

Solution:
We have to consider the negative numbers also.

Sort the numbers.
Example:
Input: 2, 10, -20, 40, -80, 20, 30, -2, -5
After sorting: -80, -20, -5, -2, 2, 10, 20, 30, 40

Now, if the array has negative numbers, they will come forward.
If absolute values of left most 2 digits are larger than the

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

Limitation:
This algorithm doesn't work for negative numbers.
E.g. -2, 2, 5, -44, 2, 1, 4
Here the max pairwise product = -2 * -44 = 88
But the algorithm will return 5 * 4 = 20

GFG has a solution for this by sorting the numbers.
"""


def max_pairwise_product(numbers):

    first_index = None
    second_index = None

    # Get the first max number
    for index, num in enumerate(numbers):
        if first_index is None:
            first_index = index

        elif num > numbers[first_index]:
            first_index = index

    # Get the second max number
    for index, num in enumerate(numbers):
        if index == first_index:
            continue

        if second_index is None:
            second_index = index

        elif num > numbers[second_index]:
            second_index = index

    max_product = numbers[first_index] * numbers[second_index]
    return max_product


def test(arr, output):
    print("Pass" if output == max_pairwise_product(arr) else "Fail")


if __name__ == '__main__':
    submit = 0
    if submit:
        input_n = int(input())
        input_numbers = [int(x) for x in input().split()]
        print(max_pairwise_product(input_numbers))

    else:
        test([2, 3, 4, 8, 10], 80)
        test([0, 2, 3, 4, 15, 1], 60)
        test([10, 20, 30, 80, 5, 9, 90, 5, 2, 1], 7200)
