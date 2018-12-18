#!/usr/bin/env python3

import re
from collections import defaultdict

def parseLine(line):
    # Pulls the two single capital letters into a tuple
    return re.search("\s([A-Z])\s.*\s([A-Z])\s", line).groups()


with open('./input.txt') as input:
    rules = [parseLine(l) for l in input.readlines()]

dag = defaultdict(list)
for r in rules:
    dag[r[1]].append(r[0])
    dag[r[0]] # make sure we create an empty list for all nodes

# start with the nodes that have no pre-reqs
candidates = sorted([k for k,v in dag.items() if v == []])

path = []
cost = {}
workers = 2
min_cost = 0
diff = ord('A')-1


def requirementsMet(k, v, c):
    if (k in path + candidates) or (c not in v):
        return False # already seen it or not valid
    # check all requirements have already been met
    return all([(req in path) for req in v])

    
while len(candidates) > 0:
    c = candidates[0]
    
    path.append(c)
    candidates = sorted(candidates[1:] + [k for k,v in dag.items() if requirementsMet(k, v, c)])
    

print("Path:", "".join(path))