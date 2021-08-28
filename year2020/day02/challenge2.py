#! /usr/bin/env python3
"""Advent of Code: Day 2
Author: Benjamin Jung
"""

import numpy as np
from collections import Counter


"""Part 1"""
print('-'*10,'Part 2', '-'*10)
def check_password(entry):
    """Check if a password conforms to the policy."""
    pwd = entry.split(':')[-1].strip(' ')
    policy = entry.split(':')[0]
    counts = Counter(pwd)
    letter = policy.split(' ')[-1]
    check = policy.split(' ')[0].split('-')
    if counts[letter] >= int(check[0]) and counts[letter] <= int(check[1]):
        return True
    else:
        return False

checklist = []
with open('password_list.txt', 'r') as infile:
    lines = infile.readlines()
    print(f'Number of passwords: {len(lines)}')
    for line in lines:
        checklist.append(check_password(line))

print(Counter(checklist))

"""Part 2"""
print('-'*10,'Part 2', '-'*10)
def recheck_password(entry):
    """Check validity of passwords according to the new
    interpretation of the policy.
    """
    pwd = entry.split(':')[-1].strip(' ')
    policy = entry.split(':')[0]
    letter = policy.split(' ')[-1]
    check = policy.split(' ')[0].split('-')
    if (pwd[int(check[0]) - 1] == letter) ^ (pwd[int(check[1]) - 1] == letter):
        return True
    else:
        return False

new_checklist = []
with open('password_list.txt', 'r') as infile:
    lines = infile.readlines()
    print(f'Number of passwords: {len(lines)}')
    for line in lines:
        new_checklist.append(recheck_password(line))

print(Counter(new_checklist))

