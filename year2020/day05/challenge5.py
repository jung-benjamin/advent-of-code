#! /usr/bin/env python 3
"""Advent of Code: Day 5
Author: Benjamin Jung
"""

import numpy as np


def decode_letters(code):
    """Decode the binary seat numbers"""
    row_list = np.arange(128)
    column_list = np.arange(8)
    for n in code:
        if n == 'F':
            row_list = row_list[:int(len(row_list) / 2)]
        elif n == 'B':
            row_list = row_list[int(len(row_list) / 2):]
        elif n == 'L':
            column_list = column_list[:int(len(column_list) / 2)]
        elif n == 'R':
            column_list = column_list[int(len(column_list) / 2):]
    
    seat_id = column_list + (8 * row_list)
    return {'row': row_list, 'column': column_list, 'seat id': seat_id}


"""Part 1"""
seat_id_list = []
with open('boarding_passes.txt', 'r') as infile:
    tickets = infile.readlines()
    for code in tickets:
        info = decode_letters(code.strip('\n'))
        seat_id_list.append(info['seat id'])

print(f'Largest seat id: {np.max(seat_id_list)}')

"""Part 2"""
max_id = np.max(seat_id_list)
min_id = np.min(seat_id_list)
for n in range(min_id, max_id + 1):
    if n not in seat_id_list:
        if ((n + 1) in seat_id_list) and ((n - 1) in seat_id_list):
            print(f'My seat id: {n}')
        else:
            pass
    else:
        pass
