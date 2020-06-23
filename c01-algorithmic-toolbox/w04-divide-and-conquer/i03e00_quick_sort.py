import sys


def partition(arr, start, end):
    left_index = start
    pivot_pos = end
    pivot_value = arr[pivot_pos]

    while (left_index != pivot_pos):

        item = arr[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        arr[left_index] = arr[pivot_pos - 1]
        arr[pivot_pos - 1] = pivot_value
        arr[pivot_pos] = item
        pivot_pos -= 1

    return pivot_pos


def quick(arr, start, end):
    if end <= start:
        return

    pivot_pos = partition(arr, start, end)
    quick(arr, start, pivot_pos - 1)
    quick(arr, pivot_pos + 1, end)


def quicksort(arr):
    quick(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    submit = 0

    if submit:
        input = sys.stdin.read()
        n, *arr = list(map(int, input.split()))
        quicksort(arr)
        for x in arr:
            print(x, end=' ')

    else:
        arr = [7, 8, 95, 2, 6, 8, 5, 4]
        quicksort(arr)
        print(arr)
