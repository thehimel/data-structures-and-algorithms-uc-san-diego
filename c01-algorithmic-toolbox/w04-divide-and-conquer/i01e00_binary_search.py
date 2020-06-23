"""
You are given an array to search from.
You are given another array of targets.
Return an array consisting of the indexes of the targets in the given array.

Example:
arr = [1, 5, 8, 12, 13]
targets = [8, 1, 23, 1, 11]
output = [2, 0, -1, 0, -1]

Target 8 is presented on index 2. Target 1 is presented on index 0.
Target 23 is not in the given array, thus -1. And so on.
"""

import sys


def search(arr, start, end, target):
    if start > end:
        return - 1

    mid = (start + end)//2

    if arr[mid] == target:
        return mid

    elif target < arr[mid]:
        return search(arr, start, mid-1, target)

    else:
        return search(arr, mid+1, end, target)


def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    index = search(arr, start, end, target)
    return index


if __name__ == '__main__':
    submit = 0

    if submit:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        m = data[n + 1]

        arr = data[1: n + 1]
        targets = data[n + 2:]

        for target in targets:
            # replace with the call to binary_search when implemented
            print(binary_search(arr, target), end=' ')

    else:
        arr = [1, 5, 8, 12, 13]
        targets = [8, 1, 23, 1, 11]

        for target in targets:
            print(binary_search(arr, target), end=' ')
