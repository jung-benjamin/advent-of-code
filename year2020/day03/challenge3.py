#! /usr/bin/env python3
"""Advent of Code: Day 3
Author: Benjamin Jung
"""

import numpy as np
from collections import Counter


"""Part 1"""
print('-'*10,'Part 1', '-'*10)
def subtract_counter(line, counter):
    """Subtract the length of the line from the index."""
    if counter < len(line):
        return counter
    else:
        return subtract_counter(line, counter - len(line))

tree_list = []
with open('tree_map.txt', 'r') as infile:
    tree_map = infile.readlines()
    tree_map = [n.strip('\n') for n in tree_map]
    slope_length = len(tree_map)
    start = 0
    points = np.arange(slope_length) * 3
    for i, line in zip(points, tree_map):
        tree_list.append(line[int(subtract_counter(line, i))])

print(Counter(tree_list))

"""Part 2"""
print('-'*10,'Part 2', '-'*10)

def tree_counter(right_increment, down_increment):
    """Count the trees in a specific path on the map."""
    tree_list = []
    with open('tree_map.txt', 'r') as infile:
        tree_map = infile.readlines()
        tree_map = [n.strip('\n') for n in tree_map][::down_increment]
        slope_length = len(tree_map)
        start = 0
        points = np.arange(slope_length) * right_increment
        for i, line in zip(points, tree_map):
            tree_list.append(line[int(subtract_counter(line, i))])

    return Counter(tree_list)

def product(l):
    """Multiply all entries of a list"""
    prod = 1
    for i in l:
        prod *= i
    return prod

possible = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_counts = []
for n in possible:
    tree_counts.append(tree_counter(*n)['#'])
print('Counts for possible paths:', tree_counts)
print('Product of tree encounters:', product(tree_counts))
