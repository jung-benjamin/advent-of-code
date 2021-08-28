#! /usr/bin/env python3
"""Advent of Code: Day 7
Author: Benjamin Jung
"""

import numpy as np
from collections import Counter

with open('bag_rules.txt', 'r') as infile:
    lines = infile.read().splitlines()

def parse_rule(rule_string):
    """Split one line into containing and contained bags."""
    s = rule_string.split('contain')
    top_bag = s[0].strip(' ')
    contents = s[-1].split(',')
    content_dict = {}
    for n in contents:
        n = n.strip(' ')
        bag_id = ' '.join(n.split(' ')[1:]).strip('.')
        if bag_id[-1] != 's':
            bag_id += 's'
        else:
            pass
        if n.split(' ')[0] == 'no':
            num_bags = 0
        else:
            num_bags = int(n.split(' ')[0])
        content_dict[bag_id] = num_bags
    bag_rule = {top_bag: content_dict}
    return bag_rule

bag_rules = {}
for n in lines:
    rule = parse_rule(n)
    bag_rules.update(rule)

allowed_directly = []
for n, item in bag_rules.items():
    if ('shiny gold bag' in item.keys()) or ('shiny gold bags' in item.keys()):
        allowed_directly.append(n)
        print(n, item)

def find_containers(bag, bag_rules):
    """Find the bags that can contain a specified bag."""
    allowed = []
    for n, item in bag_rules.items():
        if bag in item.keys():
            allowed.append(n)
    return allowed

directly = find_containers('shiny gold bags', bag_rules)
once_removed = []
for n in directly:
    once_removed += find_containers(n, bag_rules) 
twice_removed = []
for n in once_removed:
    twice_removed += find_containers(n, bag_rules)
thrice_removed = []
for n in twice_removed:
 thrice_removed += find_containers(n, bag_rules)

start = directly.copy()
all_containers = start.copy()
while start != []:
    containers = []
    for n in start:
        containers += find_containers(n, bag_rules)
    all_containers += containers
    start = containers
print('Start',len(start))
print('This is the correct answer to part 1!!!')
print('Number of containers:', len(list(Counter(all_containers).keys())))

"""This part does not yield the correct solution!!! """
def check_for_gold(bag, bag_rules):
    """Check if a shiny gold bag can be inside a bag"""
    rule = bag_rules[bag]
    if len(rule.keys()) == 1 and 'other bags' in rule.keys():
        return False
    elif 'shiny gold bags' in rule.keys():
        return True
    else:
        for n in rule.keys():
            return check_for_gold(n, bag_rules)

def list_contents(bag_rules):
    """List the contents of each bag in the rules"""
    bag_contents = {}
    contents = []
    def get_all_contents(bag, bag_rules):
        """Get all contents of a bag"""
        rule = bag_rules[bag]
        nonlocal contents
        if len(rule.keys()) == 1 and 'other bags' in rule.keys():
            return 1
        else:
            contents += list(rule.keys())
            for n in rule:
                return get_all_contents(n, bag_rules)
    
    for n in bag_rules:
        contents = []
        get_all_contents(n, bag_rules)
        bag_contents[n] = contents
    return bag_contents

content_all_bags = list_contents(bag_rules)
shiny_bag_counter = 0
for n, item in content_all_bags.items():
    if n == 'shiny gold bags':
        pass
    elif 'shiny gold bags' in item:
        shiny_bag_counter += 1
print('Number of bags that can contain a shiny gold bag:', shiny_bag_counter)

print('len rules:', len(list(bag_rules.keys())))
print('len rules counted', len(Counter(list(bag_rules.keys()))))

new_counter = 0
for n in bag_rules:
    new_counter += check_for_gold(n, bag_rules)
print('New counter:', new_counter)


"""Part 2"""
shiny_bag_contents = []

def get_bag_contents(bag, bag_rules):
    """Get all bags that are inside a bag"""
    content = []
    for n, item in bag_rules[bag].items():
        content += [n] * item
    return content

content_start = get_bag_contents('shiny gold bags', bag_rules)
shiny_bag_contents = content_start.copy()
while content_start != []:
    bag_contents = []
    for n in content_start:
        bag_contents += get_bag_contents(n, bag_rules)
    shiny_bag_contents += bag_contents
    content_start = bag_contents

print('Shiny bag contents', len(shiny_bag_contents))
