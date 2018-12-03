#!/usr/bin/env python3

with open('./input.txt') as f:
    all = [int(x) for x in f.readlines()]

    # Part 1 is to calculate the final frequency from all the variations
    print("Total frequency: ", sum(all))

    # Part 2 is to detect the first duplicate frequency when cycling throught the variations
    # It might take many cycles of the whole list to find the first duplicate frequency
    seen = set()
    running_total = 0
    duplicate = None
    while duplicate == None:
        for frequency in all:
            running_total = running_total + frequency
            if running_total in seen:
                duplicate = running_total
                break
            seen.add(running_total)

    print("Duplicate frequency: ", duplicate)