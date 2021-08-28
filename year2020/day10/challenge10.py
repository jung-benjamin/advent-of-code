#! /usr/bin/env python3
"""Advent of Code: Day 10
Author: Benjamin Jung
"""

import numpy as np
from collections import Counter
from itertools import combinations

adapters = np.genfromtxt('test.txt')
max_rated = np.max(adapters) + 3
adapters = np.array(list(adapters) + [0, max_rated])

"""Part 1"""

chained_adapters = np.sort(adapters)
differences = []
for i, j in zip(chained_adapters, chained_adapters[1:]):
    differences.append(j - i)
counts = Counter(differences)
print('Part 1:', counts[1] * counts[3])
print(counts)

"""Part 2"""
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

count_string = ''.join([str(int(n)) for n in differences])
count_ones = count_string.split('3')
combinations = 1
lengths_of_onesteps = []
for n in count_ones:
    lengths_of_onesteps.append(len(n))
print(lengths_of_onesteps)
for n in lengths_of_onesteps:
    #if n > 3:
    #    combinations *= factorial(n-1)
    #else:
    #    combinations *= factorial(n)
    if n == 0:
        combinations *= 1
    elif n == 1:
        combinations *= 1
    elif n == 2:
        combinations *= 2
    elif n == 3:
        combinations *= 5
    elif n== 4:
        combinations *= 7
print(combinations)
print('Combinations:', factorial(counts[1]) / factorial(2))

print('-'*30)
print(len(differences))
print(len(chained_adapters))
num_droppable_2s = 0
num_droppable_1s = 0
for dif, next in zip(differences, differences[1:]):
    if dif == 2 and next == 1:
        num_droppable_2s +=1
    elif dif == 1 and next == 2:
        num_droppable_1s +=1
    elif dif == 1 and next == 1:
        num_droppable_1s += 1
print(num_droppable_2s)
print('Pow:',2**num_droppable_2s)
print(num_droppable_1s)
print('Pow:', 2**num_droppable_1s)

print(np.log(19208)/np.log(2))
