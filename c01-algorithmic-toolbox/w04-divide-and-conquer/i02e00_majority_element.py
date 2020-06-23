"""
You are given an array of integers.
Check whether there is any number, that exists majority times. If so,
return 1, else return 0.
Condition of being majority is to present more than n/2 times.
n = length of the array.

Solution:
Take a dictionary counts.
For each number in the array, count it's occurance.
If there exists any number in the dictionary having count more than n/2,
return 1, else return 0.

TC: O(n)
SC: O(n)
"""

import sys


def majority_exists(arr):
    counts = dict()

    for num in arr:
        if num in counts.keys():
            counts[num] += 1
        else:
            counts[num] = 1

    half = len(arr)//2

    for num in counts:
        if counts[num] > half:
            return 1

    return 0


def test(arr, output):
    print("Pass" if majority_exists(arr) == output else "Fail")


if __name__ == '__main__':
    submit = 0
    if submit:
        input = sys.stdin.read()
        n, *arr = list(map(int, input.split()))
        print(majority_exists(arr))

    else:
        test([2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1], 1)
        test([2, 3, 9, 2, 2], 1)
        test([1, 2, 3, 4], 0)
        test(
            [512766168, 717383758, 5, 126144732, 5,
                573799007, 5, 5, 5, 405079772], 0)
