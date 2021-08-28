#! /usr/bin/env python3
"""Advent of Code: Day 9
Author: Benjamin Jung
"""

import numpy as np
from itertools import combinations

numbers = np.genfromtxt('numbers.txt')


"""Part 1"""

def check_sum(idx, numlist):
    """Check if the condition for the i-th number is met.

    The i-th number must be a sum of any two of the previous
    25 numbers.
    """
    checks = []
    for i, j in combinations(numlist[idx-25:idx], 2):
        checks.append((i + j) == numlist[idx])
    if np.any(checks):
        return True
    return False

for i, n in enumerate(numbers[25:]):
    i += 25
    if not check_sum(idx = i, numlist = numbers):
        invalid = n
        break

print('Invalid number', invalid)

"""Part 2"""
def check_list_sum(sublist, num):
    """Check if the sum of sublist is equal to the number."""
    if np.sum(sublist) == num:
        return True
    return False

weak_list = []
for i in range(len(numbers)):
    for j in range(len(numbers[i:])):
        if check_list_sum(numbers[i:j], invalid):
            weak_list.append(numbers[i:j])

print(len(weak_list[0]))
weakness = np.min(weak_list[0]) + np.max(weak_list[0])
print('Weakness:', weakness)
