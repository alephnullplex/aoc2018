#!/usr/bin/env python3

from collections import Counter

def manhatten_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def parseCoords(s):
    return tuple(map(int, s.split(',')))

with open('./input.txt') as input:
    coords = sorted([parseCoords(x) for x in input.readlines()])
    max_x = max(x[0] for x in coords)
    max_y = max(x[1] for x in coords)

    print("Field size (x, y): ", max_x, max_y)

    md = {}
    for x in range(0, max_x):
        for y in range(0, max_y):
            distances = sorted([(manhatten_distance((x, y), z), z) for z in coords])
            # check if there is only one minimum
            if distances[0][0] != distances[1][0]:
                md[(x, y)] = distances[0][1]

    # strip boundaries
    for x in range(0, max_x):
        md = { k:v for k, v in md.items() if v != md.get((x, 0), ()) and v != md.get((x, max_y), ()) }
    for y in range(0, max_y):
        md = { k:v for k, v in md.items() if v != md.get((0, y), ()) and v != md.get((max_x, y), ()) }
    
    counter = Counter(md.values())
    print("Largest finite area: ", counter.most_common(1))

    safe_region = 0
    distance_target = 10000
    for x in range(0, max_x):
        for y in range(0, max_y):
            if sum([manhatten_distance((x, y), z) for z in coords]) < distance_target:
                safe_region += 1 
    print("Safe zone: ", safe_region)



