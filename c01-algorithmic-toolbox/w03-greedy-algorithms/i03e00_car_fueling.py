"""
You are going from one city to another city situated at d distance.
There are few fuel stations at the given distances. The tank capacity is given.
Car starts with full tank. Find the minimum number of tank refill needed.

Input: distance, tank_capacity, stops = 950, 400, [200, 375, 550, 750]
Output: 2

The distance between the cities is 950, the car can travel at most 400 miles
on a full tank. It refills 2 times: at points 375 and 750. This is the minimum
number of refills.
"""

import sys


def compute_min_refills(distance, tank_capacity, stops):

    # We are mutating the stops by adding 0 at the beginning
    # and distance at the end which is our destination.
    stops = [0] + stops + [distance]

    count = 0
    stops_count = len(stops)
    remaining_fuel = tank_capacity

    # for(i=0; i < n-1; i++)
    # Considering the i+1, we'll run the for loop until the second last index.
    for i in range(stops_count-1):
        # Sub path that we need to go
        sub_path = stops[i+1] - stops[i]

        # If distance between any 2 stops greater than the capacity return -1.
        if sub_path > tank_capacity:
            return -1

        # If our remaining fuel is not enough to cover the sub_path,
        # refill it, and it becomes fill again.
        if remaining_fuel < sub_path:
            count += 1
            remaining_fuel = tank_capacity

        # After covering the sub_path, our remaining_fuel is reduced
        remaining_fuel -= sub_path

    return count


def test():
    distance, tank_capacity, stops = 950, 400, [200, 375, 550, 750]
    print(compute_min_refills(distance, tank_capacity, stops))

    distance, tank_capacity, stops = 10, 3, [1, 2, 5, 9]
    print(compute_min_refills(distance, tank_capacity, stops))


if __name__ == '__main__':
    submit = 0
    if submit:
        distance, tank_capacity, _, *stops = map(int, sys.stdin.read().split())
        print(compute_min_refills(distance, tank_capacity, stops))

    else:
        test()
