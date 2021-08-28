#! /usr/bin/env python3
"""Advent of Code: Day 14
Author: Benjamin Jung
"""

import re
import numpy as np
from collections import Counter
from itertools import combinations

def apply_mask(mask, binary):
    """Apply a bitmask to a binary number"""
    applied = []
    for i, j in zip(mask, binary):
        if i == 'X':
            applied.append(j)
        else:
            applied.append(i)
    return ''.join(applied)

def apply_memory_mask(mask, binary):
    """Apply the bitmask to the memory locations"""
    no_x = Counter(mask)['X']
    applied = np.zeros((2**no_x, len(binary))).astype(str)
    x_count = 0
    len_0 = applied.shape[0]
    
    def complex_slices(array, num):
        zeros = []
        ones = []
        one = 1
        for i in range(0, len(array), num):
            if one:
                ones += list(array[i:i+num])
                one = 0
            elif not one:
                zeros += list(array[i:i+num])
                one = 1
        return zeros, ones

    for n, (i, j) in enumerate(zip(mask, binary)):
        if i == '0':
            applied[:,n] = j
        elif i == '1':
            applied[:,n] = '1'
        elif i == 'X':
            x_count += 1
            zeros, ones = complex_slices(np.arange(len_0), int(len_0 / (2**x_count)))
            applied[zeros,n] = np.zeros(len(zeros)).astype(int).astype(str)
            applied[ones,n] = np.ones(len(ones)).astype(int).astype(str)

    return [''.join(n) for n in applied]

def mem_loc(mem_id):
    """Return the memory location"""
    loc = re.search('\d+', mem_id)
    return loc.group()

if __name__ == '__main__':
    with open('initialization.txt', 'r') as infile:
        lines = infile.read().splitlines()

    """Part 1"""
    mem = {}
    mask = 'x' * 36
    for line in lines:
        split = line.split('=')
        split = [n.strip(' ') for n in split]
        if split[0] == 'mask':
            mask = split[1]
        else:
            loc = mem_loc(split[0])
            entry = apply_mask(mask, format(int(split[1]), 'b').zfill(36))
            mem[loc] = int(entry, 2)

    mem_sum = 0
    for n, entry in mem.items():
        mem_sum += entry

    print(mem_sum)

    """Part 2"""
    mem = {}
    mask = 'x' * 36
    for line in lines:
        split = line.split('=')
        split = [n.strip(' ') for n in split]
        if split[0] == 'mask':
            mask = split[1]
        else:
            loc = format(int(mem_loc(split[0])), 'b').zfill(36)
            entry = int(split[1].strip(' '))
            mask_loc = apply_memory_mask(mask, loc)
            for n in mask_loc:
                mem[n] = entry

    mem_sum = 0
    for n, entry in mem.items():
        mem_sum += entry

    print(mem_sum)

