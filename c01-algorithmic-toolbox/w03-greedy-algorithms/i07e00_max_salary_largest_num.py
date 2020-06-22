"""
Task: Compose the largest number out of a set of integers.

input = [8, 3, 1, 7, 0, 10, 2]
output = "87321100"

input = [21, 2]
output = "221"

input = [9, 4, 6, 1, 9]
output = "99641"

input = [23, 39, 92]
output = "923923"


Solution:
It uses merge sort, for sorting the array.
Remember, in merge sort, suppose we are sorting the numbers from max to min,
then if the left number is larger than the right one, then we add it to the
array first. In this case we'll see, if we can keep the left number first.

Consider 89 and 224.
In this case, the possible two numbers are: 89224 and 22489.
So, keeping the larger number on left won't make the number larger.
If the max digit of the left number is larger than that of the right number,
then keeping the left number on left will make the number larger. So, for 89,
max digit is 89. and for 224, max digit is 4. Thus, 89 should be left.

Now, another case is there. Consider 21 and 2. In this case, max digit of the
both numbers are same. So, if 21 is the left in the array, the merge sort will
put 21 first and it will become 212, which is not true. here 221 is larger.

So, we actually, need to form strings combining these 2 numbers, and if
keeping the left number left makes the larger number, then we'll keep the
left number on left.

arr = [21, 2]
x = 21, y = 2
xy = '212', yx = '212'
return xy > yx

TC: O(nlogn)
SC: O(n)
"""

import sys


def max_digit(num):
    largest_digit = None

    if num < 10:
        return num

    while(num > 0):
        last_digit = num % 10

        if largest_digit is None:
            largest_digit = last_digit

        else:
            if last_digit > largest_digit:
                largest_digit = last_digit

        num = num//10

    return largest_digit


def keep_left_first(x, y):
    if max_digit(x) > max_digit(y):
        return True

    elif max_digit(x) == max_digit(y):
        xy = int(str(x) + str(y))
        yx = int(str(y) + str(x))

        return xy > yx

    else:
        return False


def split(arr, start, end):
    if(start < end):
        mid = (start + end) // 2
        split(arr, start, mid)
        split(arr, mid+1, end)

        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    p = start
    q = mid + 1
    temp_arr = [None for _ in range(end+1 - start)]
    k = 0

    for i in range(start, end+1):
        if (p > mid):
            temp_arr[k] = arr[q]
            k += 1
            q += 1

        elif (q > end):
            temp_arr[k] = arr[p]
            k += 1
            p += 1

        # Here is the magic occurs
        elif keep_left_first(arr[p], arr[q]):
            temp_arr[k] = arr[p]
            k += 1
            p += 1

        else:
            temp_arr[k] = arr[q]
            k += 1
            q += 1

    k = 0
    while(k < len(temp_arr)):
        arr[start] = temp_arr[k]
        start += 1
        k += 1


def mergesort(arr):
    split(arr, 0, len(arr) - 1)


"""
# Test merge_sort
arr2 = [8, 3, 1, 7, 0, 10, 2]
arr3 = [1, 0]
arr4 = [97, 98, 99]
arr5 = [85, 22, 11111]

mergesort(arr2)
mergesort(arr3)
mergesort(arr4)
mergesort(arr5)
"""


def largest_number(arr):
    mergesort(arr)

    output = ""
    for num in arr:
        output += str(num)

    # print(output)
    return output


def test(input, output):
    print("Pass" if output == largest_number(input) else "Fail")


if __name__ == '__main__':
    submit = 0

    if submit:
        input = sys.stdin.read()
        data = input.split()
        a = data[1:]
        arr = [int(num) for num in a]
        print(largest_number(arr))

    else:
        input = [8, 3, 1, 7, 0, 10, 2]
        output = "87321100"
        test(input, output)

        input = [21, 2]
        output = "221"
        test(input, output)

        input = [9, 4, 6, 1, 9]
        output = "99641"
        test(input, output)

        input = [23, 39, 92]
        output = "923923"
        test(input, output)
