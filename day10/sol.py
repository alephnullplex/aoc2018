#!/usr/bin/env python3

import re

PX = 0
PY = 1
VX = 2
VY = 3

def parseLine(line):
    return list(map(int, re.findall(r"[\d-]+", line)))

def boundingBox(grid):
    x = [p[PX] for p in grid]
    y = [p[PY] for p in grid]
    return (max(x) - min(x)) * (max(y) - min(y))

def step(grid):
    return [[px + vx, py + vy, vx, vy] for px, py, vx, vy in grid]

with open('input.txt') as input:
    points = list(map(parseLine, input.readlines()))

bb = boundingBox(points)
time = 0
while True:
    new_points = step(points)
    new_bb = boundingBox(new_points)

    if new_bb < bb:
        bb = new_bb
        points = new_points
        time += 1
    else:
        break

x = [p[PX] for p in points]
y = [p[PY] for p in points]
final = set((p[PX], p[PY]) for p in points)


# simple matrix printer
print("After {} secs this message will appear:".format(time))
for i in range(min(y), max(y)+1):
    for j in range(min(x), max(x)+1):
        print("X" if (j,i) in final else ' ', end="")
    print()