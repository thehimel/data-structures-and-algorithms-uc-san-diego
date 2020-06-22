"""
Ref: https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/
"""

import sys


def comparator(x, y):
    xy = str(x) + str(y)
    yx = str(y) + str(x)
    return ((int(yx) > int(xy)) - (int(yx) < int(xy)))


def compare(the_comparator):
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return the_comparator(self.obj, other.obj) < 0

        def __gt__(self, other):
            return the_comparator(self.obj, other.obj) > 0

        def __eq__(self, other):
            return the_comparator(self.obj, other.obj) == 0

        def __le__(self, other):
            return the_comparator(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return the_comparator(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return the_comparator(self.obj, other.obj) != 0

    return K


def largest_number(arr):
    sorted_array = sorted(arr, key=compare(comparator))
    number = "".join([str(i) for i in sorted_array])
    return number


def test(input, output):
    print("Pass" if output == largest_number(input) else "Fail")


if __name__ == '__main__':
    submit = 0

    if submit:
        input = sys.stdin.read()
        data = input.split()
        a = data[1:]
        arr = [int(num) for num in a]
        print(largest_number(a))

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
