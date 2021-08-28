#! /usr/bin/env python3
"""Advent of Code: Day 8
Author: Benjamin Jung
"""

import numpy as np
import pandas as pd

with open('console_code.txt', 'r') as infile:
    lines = infile.read().splitlines()

instructions = []
increment = []
for n in lines:
    instructions.append(n.split(' ')[0])
    increment.append(int(n.split(' ')[1]))

code_df = pd.DataFrame(np.array([instructions, increment]).T, 
                       columns = ['instructions', 'increment'],
                       )
code_df['counter'] = np.zeros(len(code_df))
code_df['increment'] = code_df['increment'].astype(int)

"""Part 1"""
accumulator = 0
i = 0
while i <= len(code_df):
    code_df.loc[i,'counter'] += 1
    row = code_df.loc[i,:]
    if row['counter'] > 1:
        print('Accumulator:', accumulator)
        break
    elif row['instructions'] == 'nop':
        i+=1
    elif row['instructions'] == 'acc':
        accumulator += row['increment']
        i+=1
    elif row['instructions'] == 'jmp':
        i += row['increment']

"""Part 2"""
def check_code(code):
    """Check to see if the code is broken."""
    accumulator = 0
    i = 0
    while i < len(code):
        code.loc[i,'counter'] += 1
        row = code.loc[i,:]
        if row['counter'] > 1:
            print('Accumulator:', accumulator)
            return False, accumulator
        elif row['instructions'] == 'nop':
            i+=1
        elif row['instructions'] == 'acc':
            accumulator += row['increment']
            i+=1
        elif row['instructions'] == 'jmp':
            i += row['increment']
    return True, accumulator 

code_df['counter'] = np.zeros(len(code_df))
for j, row in code_df.iterrows():
    test_code = code_df.copy()
    test_code['counter'] = np.zeros(len(test_code))
    if row['instructions'] == 'acc':
        pass
    elif row['instructions'] == 'nop' and row['increment'] == 0:
        pass
    elif row['instructions'] == 'nop':
        test_code.loc[j, 'instructions'] = 'jmp'
        test = check_code(test_code)
        if test[0]:
            print('Fixed accumulator:', test[1])
            break
    elif row['instructions'] == 'jmp':
        test_code.loc[j, 'instructions'] = 'nop'
        test = check_code(test_code)
        if test[0]:
            print('Fixed accumulator:', test[1])
            break
