import sys


def count_inversions(arr):
    start = 0
    end = len(arr) - 1
    output = inversion_count_func(arr, start, end)
    return output


def inversion_count_func(arr, start, end):
    if start >= end:
        return 0

    mid = start + (end - start) // 2

    # find number of inversions in left-half
    left_answer = inversion_count_func(arr, start, mid)

    # find number of inversions in right-half
    right_answer = inversion_count_func(arr, mid + 1, end)

    output = left_answer + right_answer

    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(
        arr, start, mid, mid + 1, end)
    return output


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_index = start_one
    right_index = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_index] <= arr[right_index]:
            output_list[index] = arr[left_index]
            left_index += 1

        else:
            # left > right hence it's an inversion
            count = count + (end_one - left_index + 1)
            output_list[index] = arr[right_index]
            right_index += 1

        index = index + 1

        if left_index > end_one:
            for i in range(right_index, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_index > end_two:
            for i in range(left_index, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break

    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    return count


def test(input, output):
    print("Pass" if output == count_inversions(input) else "Fail")


if __name__ == '__main__':
    submit = 0

    if submit:
        input = sys.stdin.read()
        n, *arr = list(map(int, input.split()))
        b = n * [0]
        print(count_inversions(arr))

    else:
        test([2, 5, 1, 3, 4], 4)
        test([54, 99, 49, 22, 37, 18, 22, 90, 86, 33], 26)
        test([1, 2, 4, 2, 3, 11, 22, 99, 108, 389], 2)
