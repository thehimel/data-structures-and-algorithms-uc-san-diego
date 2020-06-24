# https://www.techiedelight.com/3-partition-problem/

import sys


def subset(numbers, n, f, s, t):
    if sum(numbers) % 3 != 0:
        return False

    if f == 0 and s == 0 and t == 0:
        return True

    if n < 0:
        return False

    First = False
    if f - numbers[n] >= 0:
        First = subset(numbers, n - 1, f - numbers[n], s, t)

    Second = False
    if not First and (s - numbers[n] >= 0):
        Second = subset(numbers, n - 1, f, s - numbers[n], t)

    Third = False
    if (not First and not Second) and (t - numbers[n] >= 0):
        Third = subset(numbers, n - 1, f, s, t - numbers[n])

    return First or Second or Third


def partition3(numbers):

    if len(numbers) < 3:
        return False

    partition_sum = sum(numbers) / 3
    return subset(
        numbers, len(numbers) - 1, partition_sum, partition_sum, partition_sum)


def partition(numbers):
    return 1 if partition3(numbers) is True else 0


def test(input, output):
    print("Pass" if output == partition(input) else "Fail")


if __name__ == '__main__':
    submit = 0
    if submit:
        input = sys.stdin.read()
        n, *numbers = list(map(int, input.split()))
        print(partition(numbers))

    else:
        test([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], 0)
        test([3, 3, 6, 5, -2, 2, 5, 1, -9, 4], 1)

        test([3, 3, 3, 3], 0)
        test([40], 0)
        test([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59], 1)
        test([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25], 1)
