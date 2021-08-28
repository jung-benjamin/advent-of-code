#! /usr/bin/env python3
"""Advent of Code: Day 4
Author: Benjamin Jung
"""

import re
import numpy as np
from itertools import groupby
from collections import Counter

"""Part 1"""
print('-'*10, 'Part 1', '-'*10)
with open('passport_list.txt', 'r') as res:
            lines = res.readlines()

i = (list(g) for _, g in groupby(lines, key='\n'.__ne__))
passports = [a for a, _ in zip(i, i)]

def process_passport(passport):
    """Turn a passport list into a dictionary."""
    pass_string = ' '.join([n.strip('\n') for n in passport])
    pass_list = pass_string.split(' ')
    pass_dict = {}
    for n in pass_list:
        key, entry = n.split(':')
        pass_dict[key] = entry
    
    return pass_dict

expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
#cid is not expected, because we want to get through the control
def validate(pass_dict):
    """Validate a passport."""
    value = []
    for n in expected_fields:
        value.append(n in pass_dict.keys())
    return np.all(value)

valid_id = []
validated = []
for p in passports:
    proc = process_passport(p)
    valid = validate(proc)
    if valid:
        valid_id.append(proc)
    validated.append(valid)

print(Counter(validated))

"""Part 2"""
print('-'*10, 'Part 2', '-'*10)

def valid_year(entry, minimum, maximum):
    """Validate four digit year entries."""
    if len(entry) > 4:
        return False
    elif int(entry) >= minimum and int(entry) <= maximum:
        return True
    else:
        return False

def valid_hgt(entry):
    """Validate height entries."""
    if entry[-2:] == 'cm':
        if int(entry[:-2]) >= 150 and int(entry[:-2]) <= 193:
            return True
        else:
            return False
    elif entry[-2:] == 'in':
        if int(entry[:-2]) >= 59 and int(entry[:-2]) <= 76:
            return True
        else:
            return False
    else:
        return False

def valid_hcl(entry):
    """Validate hair color entries"""
    if entry[0] == '#':
        if len(entry) == 7:
            check = re.match(r'[^a-f0-9]', entry[1:])
            if check is None:
                return True
            else:
                return False
        else:
            return False
    else: 
        return False

def valid_ecl(entry):
    """Validate eye color entries"""
    valid_entries = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if entry in valid_entries:
        return True
    else:
        return False

def valid_pid(entry):
    """Validate pid entries"""
    if len(entry) == 9:
        check = re.match(r'\D', entry)
        if check is None:
            return True
        else:
            return False
    else:
        return False

validation_maps = {'byr': lambda x: valid_year(x, 1920, 2002),
                   'iyr': lambda x: valid_year(x, 2010, 2020),
                   'eyr': lambda x: valid_year(x, 2020, 2030),
                   'hgt': valid_hgt,
                   'hcl': valid_hcl,
                   'ecl': valid_ecl,
                   'pid': valid_pid,
                   }

def validate_entries(pass_dict):
    """Validate all entries of a passport"""
    validation_list = []
    for n, entry in pass_dict.items():
        if n == 'cid':
            pass
        else:
            validation_list.append(validation_maps[n](entry))
    return np.all(validation_list)

validated_passports = []
for p in valid_id:
    validated_passports.append(validate_entries(p))

print(Counter(validated_passports))
