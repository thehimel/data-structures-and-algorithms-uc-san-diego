"""
https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/

Find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 3 and 4.
"""

import sys


def money_change(coins, coins_count, money):
    table = [0 for i in range(money + 1)]

    table[0] = 0

    for i in range(1, money + 1):
        table[i] = sys.maxsize

    for i in range(1, money + 1):
        for j in range(coins_count):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (
                    sub_res != sys.maxsize and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    return table[money]


def get_change(money):
    coins = [1, 3, 4]
    coins_count = len(coins)
    return money_change(coins, coins_count, money)


def test(input, output):
    print("Pass" if output == get_change(input) else "Fail")


if __name__ == '__main__':
    submit = 0
    if submit:
        m = int(sys.stdin.read())
        print(get_change(m))

    else:
        test(2, 2)
        test(34, 9)
