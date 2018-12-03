#!/usr/bin/env python3

import re
from collections import Counter

with open("./input.txt") as input:
    claims = input.readlines()

    # some consts for easier indexing
    ID = 0
    X = 1
    Y = 2
    W = 3
    H = 4
    
    # each claim is 5 numbers with punctuation
    # just grab the numbers and ditch all the punctiation
    # [id, x, y, width, height]
    claims = [list(map(int, re.findall(r"[\d]+", c))) 
                 for c in claims]
    
    # this is pretty brute force
    # it creates a list of every co-ordinate in every claim
    all_coords = [(i, j)
        for c in claims
            for i in range(c[X], c[X] + c[W])
                for j in range(c[Y], c[Y] + c[H])]
    
    # count the claims on each co-ordinate
    claim_count = Counter(all_coords)
    print("Multiple claims: ", sum(1 for k,v in claim_count.items() if v > 1))

    # brute force part 2 with some basic short circuiting
    for c in claims:
        dup = False
        for i in range(c[X], c[X] + c[W]):
            if dup:
                break 
            for j in range(c[Y], c[Y] + c[H]):
                if claim_count[(i,j)] > 1:
                    dup = True
                    break
        if not dup:
            print("Found claim:", c[ID])
            break