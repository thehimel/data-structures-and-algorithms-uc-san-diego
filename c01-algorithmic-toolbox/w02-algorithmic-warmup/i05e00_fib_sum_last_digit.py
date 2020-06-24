# https://www.geeksforgeeks.org/sum-fibonacci-numbers/

import sys


def fib_sum_last(n):
    if (n <= 0):
        return 0

    fib_i_2 = 0
    fib_i_1 = 1

    sum = fib_i_1 + fib_i_2

    for i in range(2, n+1):
        fib = (fib_i_1 + fib_i_2) % 10
        fib_i_1, fib_i_2 = fib, fib_i_1
        sum = sum + fib

    return sum % 10


def test(input, output):
    print("Pass" if output == fib_sum_last(input) else "Fail")


if __name__ == "__main__":
    submit = 0

    if submit:
        input = sys.stdin.read()
        n = int(input)
        print(fib_sum_last(n))

    else:
        test(3, 4)
        test(100, 5)
        test(613455, 6)
