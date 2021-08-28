#! /usr/bin/env python3
"""Advent of Code: Day 6
Author: Benjamin Jung
"""

import numpy as np
from itertools import groupby
from collections import Counter

with open('customs_forms.txt', 'r') as infile:
    lines = infile.readlines()

i = (list(g) for _, g in groupby(lines, key='\n'.__ne__))
answers = [a for a, _ in zip(i, i)]


"""Part 1"""

def count_answers(group):
    """Count the number of positive answers of a group."""
    line = ''.join([n.strip('\n') for n in group])
    count = Counter(line)
    number = len(count.keys())
    return number

all_numbers = [count_answers(n) for n in answers]
print(np.sum(all_numbers))

"""Part 2"""
def recount_answers(group):
    """Count the number of positive answers of a group.

    Only the questions to which everyone in a group answered
    yes to count.
    """
    people = len(group)
    line = ''.join([n.strip('\n') for n in group])
    count = Counter(line)
    number = 0
    for n, item in count.items():
        if item == people:
            number += 1
    return number

new_numbers = [recount_answers(n) for n in answers]
print('New sum:', np.sum(new_numbers))
