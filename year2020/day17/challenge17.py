#! /usr/bin/env python3
"""Advent of Code: Day 17
Author: Benjamin Jung
"""

import numpy as np
from itertools import product, combinations, combinations_with_replacement

def get_surroundings(array, coord):
    """Get the surroundings a box in an array"""
    x_len, y_len, z_len = array.shape
    for i, j, k in combinations_with_replacement(range(len(coord)), r = 3):
        print(i, j, k)
    

if __name__ == '__main__':
    with open('initial.txt', 'r') as infile:
        lines = infile.read().splitlines()
        initial = np.array([list(n) for n in lines])
    
    filler = np.zeros(initial.shape).astype(str)
    for i, j in product(range(filler.shape[0]), range(filler.shape[1])):
        filler[i,j] = '.'

    start = np.array([filler, initial, filler])

    get_surroundings(start, [1, 2, 3])
