#! /usr/bin/env python3
"""Advent of Code: Day 11
Author: Benjamin Jung
"""

import numpy as np
from collections import Counter
from itertools import product

with open('seat_layout.txt', 'r') as infile:
    lines = infile.read().splitlines()
    layout = [list(line) for line in lines]
layout = np.array(layout)

print(layout[0,0])

def get_adjacent(x, y, layout):
    """Get coordinates of seats adjacent to a seat"""
    #x_max = len(layout[0] - 1)
    #x_min = 0
    #y_max = len(layout) - 1
    #y_min = 0
    
    sides = [(x - 1, y), (x + 1, y)]
    top = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
    bottom = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    adjacent = top + sides + bottom
    content = []
    for n in adjacent:
        try:
            c = layout[n[0], n[1]]
            if n[1] < 0 or n[0] < 0:
                pass
            else:
                content.append(c)
        except IndexError: 
            pass
    return np.array(content)

def apply_rules(x, y, layout):
    """Apply the seating rules to a seat"""
    seat = layout[x, y]
    surroundings = get_adjacent(x, y, layout)
    new_seat = seat
    if seat == 'L':
        if '#' not in surroundings:
            new_seat = '#'
    elif seat == '#':
        count = Counter(surroundings)
        if count['#'] > 3:
            new_seat = 'L'

    return new_seat

"""Part 1"""

def update_seats(layout):
    """Update all seats according to the rules"""
    y_range = range(len(layout[0]))
    x_range = range(len(layout))
    update = layout.copy()
    for x, y in product(x_range, y_range):
        seat_update = apply_rules(x, y, layout)
        update[x, y] = seat_update
    return update

seat_map = layout.copy()
same = 0
counter = 0
while not same:
    new_map = update_seats(seat_map)
    same = np.all(seat_map == new_map)
    seat_map = new_map
    counter += 1

print(counter)
occupied = Counter(seat_map.flatten())['#']
print(occupied)

"""Part 2"""

def get_visible(x, y, layout):
    """Get coordinates of nearest visible seats"""
    x_max = len(layout) - 1
    y_max = len(layout[0]) - 1

    def get_left(x, y, layout):
        n = (x, y - 1)
        if n[1] < 0:
            return None
        elif layout[n] == '#' or layout[n] == 'L':
            return layout[n]
        else:
            return get_left(x, y - 1, layout)
    
    def get_right(x, y, layout):
        n = (x, y + 1)
        if n[1] > y_max:
            return None
        elif layout[n] == '#' or layout[n] == 'L':
            return layout[n]
        else:
            return get_right(x, y + 1, layout)

    def get_up(x, y, layout):
        n = (x - 1, y)
        if n[0] < 0:
            return None
        elif layout[n] == '#' or layout[n] == 'L':
            return layout[n]
        else:
            return get_up(x - 1, y, layout)

    def get_down(x, y, layout):
        n = (x + 1, y)
        if n[0] > x_max:
            return None
        elif layout[n] == '#' or layout[n] == 'L':
            return layout[n]
        else:
            return get_down(x + 1, y, layout)
    
    def get_down_left(x, y, layout):
        n = (x + 1, y - 1)
        if n[0] > x_max or n[1] < 0:
            return None
        elif layout[n] == '#' or layout[n] == 'L':
            return layout[n]
        else:
            return get_down_left(x + 1, y - 1, layout)

    def get_up_left(x, y, layout):
        n = (x - 1, y - 1)
        if n[1] < 0 or n[0] < 0:
            return None
        elif layout[n] == '#' or layout[n] == 'L':
            return layout[n]
        else:
            return get_up_left(x - 1, y - 1, layout)

    def get_down_right(x, y, layout):
        n = (x + 1, y + 1)
        if n[1] > y_max or n[0] > x_max:
            return None
        elif layout[n] == '#' or layout[n] == 'L':
            return layout[n]
        else:
            return get_down_right(x + 1, y + 1, layout)

    def get_up_right(x, y, layout):
        n = (x - 1, y + 1)
        if n[1] > y_max or n[0] < 0:
            return None
        elif layout[n] == '#' or layout[n] == 'L':
            return layout[n]
        else:
            return get_up_right(x - 1, y + 1, layout)

    content = []
    content.append(get_up_right(x, y, layout))
    content.append(get_up_left(x, y, layout))
    content.append(get_down_right(x, y, layout))
    content.append(get_down_left(x, y, layout))
    content.append(get_up(x, y, layout))
    content.append(get_down(x, y, layout))
    content.append(get_left(x, y, layout))
    content.append(get_right(x, y, layout))

    return np.array(content)

def new_rules(x, y, layout):
    """Apply the seating rules to a seat"""
    seat = layout[x, y]
    surroundings = get_visible(x, y, layout)
    new_seat = seat
    if seat == 'L':
        if '#' not in surroundings:
            new_seat = '#'
    elif seat == '#':
        count = Counter(surroundings)
        if count['#'] > 4:
            new_seat = 'L'

    return new_seat

def new_update_seats(layout):
    """Update all seats according to the rules"""
    y_range = range(len(layout[0]))
    x_range = range(len(layout))
    update = layout.copy()
    for x, y in product(x_range, y_range):
        seat_update = new_rules(x, y, layout)
        update[x, y] = seat_update
    return update


seat_map = layout.copy()
same = 0
counter = 0
while not same:
    new_map = new_update_seats(seat_map)
    same = np.all(seat_map == new_map)
    seat_map = new_map
    counter += 1

print(counter)
occupied = Counter(seat_map.flatten())['#']
print(occupied)

