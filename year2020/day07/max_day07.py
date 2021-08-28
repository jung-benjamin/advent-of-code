import re

def define_bag(bag):
    """Define a bag, i.e. assign its color and rules"""

    # Remove all spaces and the final period and linebreak.
    bag = bag.replace(" ", "")[:-2]
    
    name, contents = bag.split("bagscontain")
    contents = get_rules(contents)

    return name, contents

def get_rules(content):
    """Get rules for a bag. If it is empty, return None"""
    
    if "noother" in content:
        return None
    content = content.split(",")
    rules = {}
    for rule in content:
        rule = rule.replace("bags", "").replace("bag", "")
        quantity = re.compile("\d{1,2}").match(rule)[0]
        name = re.compile("[a-z]+").search(rule)[0]

        rules[name] = int(quantity)
    
    return rules

def find_gold_bag(colour, bags):
    #print(f"Opening bag of colour {colour}")
    content = bags[colour]
    if content is None:
        return 0
    
    if "shinygold" in content.keys():
        return 1
    
    for bag in content.keys():
        if find_gold_bag(bag, bags):
            return 1
    
    return 0

def bags_in_bag(colour, bags): 
    content = bags[colour]
    
    if content is None:
        return 1
    
    bags_inside = 0
    for bag in content.keys():
        bags_inside += bags[colour][bag] * bags_in_bag(bag, bags)

    return bags_inside + 1

def main():
    fname = "input/day07.txt"
    #fname = "test.txt"
    
    bags = {}
    
    # Read in data, create bags and rules etc.
    with open(fname, "r") as f:
        for bag in f:
            color, rule = define_bag(bag)
            bags[color] = rule
    print(f"In total, {len(list(bags.keys()))} different bags exist.")

    # Part 1
    contains_shinygold = 0
    for bag in bags.keys():
        if bag=="shinygold":
            continue
        contains_shinygold += find_gold_bag(bag, bags)
    print(f"Eventually, {contains_shinygold} bags can contain a shinygold bag.")
    
    # Part 2, subtract 1 because the shiny gold bag itself is not counted
    bags_inside = bags_in_bag("shinygold", bags) - 1
    print(f"{bags_inside} bags inside 1 shinygold bag.")
    
    
if __name__=="__main__":
    main()


