# https://github.com/thehimel/data-structures-and-algorithms-udacity/blob/master/m04c03-dynamic-programming/i05e00_longest_cmn_subsequence.py

import sys


def lcs(string_a, string_b):
    b = len(string_b) + 1
    a = len(string_a) + 1
    lookup_table = [[0] * b] * a

    for char_a_i, char_a in enumerate(string_a):

        for char_b_i, char_b in enumerate(string_b):
            if char_a == char_b:
                top_left_cell = lookup_table[char_a_i][char_b_i]
                lookup_table[char_a_i + 1][char_b_i + 1] = top_left_cell + 1

            else:
                left_cell = lookup_table[char_a_i][char_b_i + 1]
                top_cell = lookup_table[char_a_i + 1][char_b_i]
                max_value = max(left_cell, top_cell)

                lookup_table[char_a_i + 1][char_b_i + 1] = max_value

    return lookup_table[-1][-1]


def test(a, b, output):
    print("Pass" if output == lcs(a, b) else "Fail")


if __name__ == '__main__':
    submit = 0

    if submit:
        input = sys.stdin.read()
        data = list(map(int, input.split()))

        n = data[0]
        data = data[1:]
        a = data[:n]

        data = data[n:]
        m = data[0]
        data = data[1:]
        b = data[:m]

        print(lcs(a, b))

    else:
        a = [2, 7, 5]
        b = [2, 5]
        output = 2
        test(a, b, output)

        a = [7]
        b = [1, 2, 3, 4]
        output = 0
        test(a, b, output)

        a = [2, 7, 8, 3]
        b = [5, 2, 8, 7]
        output = 2
        test(a, b, output)

        a = []
        b = []
        output = 0
        test(a, b, output)
