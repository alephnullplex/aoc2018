#!/usr/bin/env python3
distance = ord('a') - ord('A')    

def react(polymers):
    made_replacement = True
    while made_replacement:
        made_replacement = False
        for i in range(len(polymers)-1):
            if abs(polymers[i] - polymers[i+1]) == distance:
                polymers[i] = polymers[i+1] = 0
                made_replacement = True
        polymers = [x for x in polymers if x != 0]
    return polymers

with open("./input.txt") as input:
    polymers = [ord(c) for c in input.read().strip()]

    print("initial length: ", len(polymers))
    print("Final length: ", len(react(polymers)))

    stripped = []
    print(len(polymers))
    for c in range(ord('a'), ord('z')+1):
        stripped.append([x for x in polymers if x != c and x != c-distance])
    print("Stripped min length: ", min([len(react(x)) for x in stripped]))




