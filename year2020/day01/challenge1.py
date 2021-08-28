#! /usr/bin/env/python3
"""Advent of Code: Day 1
Author: Benjamin Jung
"""

import numpy as np
from itertools import combinations

expenses = np.genfromtxt('expense_report.txt')

"""Challenge 1"""

for i, j in combinations(expenses, 2):
    if i + j == 2020:
        print(i, j, i + j, i * j)

for i, j, k in combinations(expenses, 3):
    if i + j + k == 2020:
        print(i, j, k, i + j + k, i *j * k)
