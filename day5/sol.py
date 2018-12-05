#!/usr/bin/env python3
distance = ord('a') - ord('A')    

def react(polymers):
    p = []
    for i in polymers:
        if len(p) == 0:
            p.append(i)
        if abs(p[-1] - i) == distance:
            p.pop()
        else:
            p.append(i)
    return p

with open("./input.txt") as input:
    polymers = [ord(c) for c in input.read().strip()]

    print("initial length: ", len(polymers))
    print("Final length: ", len(react(polymers[:])))

    stripped = []
    for c in range(ord('a'), ord('z')+1):
        stripped.append([x for x in polymers if x != c and x != c-distance])
    print("Stripped min length: ", min([len(react(x)) for x in stripped]))




