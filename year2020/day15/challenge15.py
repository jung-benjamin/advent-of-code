#! /usr/bin/env python3
"""Advent of Code: Day 15
Author: Benjamin Jung
"""

import numpy as np
from collections import defaultdict
from tqdm import tqdm

if __name__ == '__main__':
    starting = np.genfromtxt('starting.txt', delimiter = ',')
    index = defaultdict(list)
    
    # set the first values
    for i, n in enumerate(starting):
        index[int(n)] += [i + 1]

    last_number = int(starting[-1])
    for i in tqdm(range(7,30000001)):
        if last_number in index.keys():
            if len(index[last_number]) > 1:
                difference = index[last_number][-1] - index[last_number][-2]
            elif len(index[last_number]) == 1:
                difference = 0
        else: 
            print('ERROR - Last number not in dict')
            
        last_number = difference
        index[last_number] += [i]
    print(i, last_number)
