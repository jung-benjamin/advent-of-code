#! /usr/bin/env python3
"""Advent of Code: DAy 13
Author: Benjamin Jung
"""

import numpy as np
import math

with open('notes.txt', 'r') as infile:
    lines = infile.read().splitlines()

earliest = int(lines[0])
notes = lines[1].split(',')

"""Part 1"""

bus_ids = []
for n in notes:
    try:
        bus_ids.append(int(n))
    except:
        pass

bus_ids = np.array(bus_ids)

# number of cycles the bus has passed since start
no_cycles = earliest / bus_ids
# next departure
next_departure = np.array([math.ceil(n) for n in no_cycles]) * bus_ids
differences = next_departure - earliest

wait_time = np.min(differences)
best_bus = bus_ids[np.argmin(differences)]
solution = wait_time * best_bus
print('Departure time', next_departure[np.argmin(differences)])
print('Wait time', np.min(differences))
print('Bus id', bus_ids[np.argmin(differences)])
print('Solution part 1:', solution)

"""Part 2"""
id_list = []
for n in notes:
    try:
        id_list.append(int(n))
    except:
        id_list.append(None)
delta_t = []
for i, n in enumerate(id_list):
    if n is not None:
        delta_t.append(i)

def get_wait_times(start, bus_ids):
    """Calculate the wait time for the bus ids"""
    bus_ids = np.array(bus_ids)
    no_cycles = start / bus_ids
    next_departure = np.array([math.ceil(n) for n in no_cycles]) * bus_ids
    differences = next_departure - start
    return differences

def compare_times(start, bus_ids, delta):
    """Compare the wait time with the time deltas"""
    wait = get_wait_times(start, bus_ids)
    compare = np.all(wait == delta_t)
    return compare

#time = 100000000000000
time = 0
winner = True
counter = 0
#while winner:
#    wait = get_wait_times(time, bus_ids)
#    if np.all(wait == delta_t):
#        winner = False
#        print('Earliest timestamp:', time)
#    time += 1
#    if counter == 100000000000000:
#        break
#    counter += 1

timesteps = np.arange(time, time + 1e9)
test = compare_times(timesteps.T, bus_ids, delta_t)
