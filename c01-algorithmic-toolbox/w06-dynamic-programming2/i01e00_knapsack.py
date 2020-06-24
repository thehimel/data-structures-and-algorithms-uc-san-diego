"""
Given the weights of items and max amount of the knapsack.
Find the max weight that can be taken into the knapsack.

0-1 Knapsack Problem with Dynamic Programming
Complexity Analysis:
n = Total number of items
W = Capacity of the Knapsack
TC: O(n * W) - For every item, traversing through the array of size W.
SC: O(W) - Creating an array of size W.
"""

import sys
import collections

# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])


# DP Solution
# Get the max total value ($) of items that can be placed into the knapsack
def knapsack_max_value(knapsack_max_weight, items):

    # Initialize a lookup table to store the maximum value ($)
    lookup_table = [0] * (knapsack_max_weight + 1)

    # Iterate down the given list
    for item in items:
        # The "capcacity" represents amount of remaining capacity (kg)
        # of knapsack at a given moment.
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(
                    lookup_table[capacity],
                    lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]


def test(knapsack_max_weight, items, output):
    print("Pass" if output == knapsack_max_value(
        knapsack_max_weight, items) else "Fail")


if __name__ == '__main__':
    submit = 0
    if submit:
        input = sys.stdin.read()
        knapsack_max_weight, n, *items_weight = list(map(int, input.split()))
        items = list()

        # As value is not given, weight is considered as the value
        for weight in items_weight:
            value = weight
            items.append(Item(weight, value))

        print(knapsack_max_value(knapsack_max_weight, items))

    else:
        knapsack_max_weight = 15
        items = [Item(10, 7), Item(9, 8), Item(5, 6)]
        output = 14
        test(knapsack_max_weight, items, output)

        knapsack_max_weight = 25
        items = [
            Item(10, 2), Item(29, 10), Item(5, 7),
            Item(5, 3), Item(5, 1), Item(24, 12)]
        output = 13
        test(knapsack_max_weight, items, output)

        knapsack_max_weight = 10
        items = [Item(1, 1), Item(4, 4), Item(8, 8)]
        output = 9
        test(knapsack_max_weight, items, output)
