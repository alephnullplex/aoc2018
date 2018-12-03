#!/usr/bin/env python3

from collections import Counter

def find_off_by(distance, list):
    """ Uses the Hamming algorithm to find the first pair with a difference of `distance` """
    for i in range(len(list)):
        for j in range(i, len(list)):
            if sum(ca != cb for ca, cb in zip(list[i], list[j])) == distance:
                return (list[i], list[j])

def checksum(input):
    """ Checksum by counting items that have duplicates and/or triplicates and multiplying"""
    checksum_twos = 0
    checksum_threes = 0

    for id in input:
        c = [v for k,v in Counter(id).items()]
        if 2 in c:
            checksum_twos += 1
        if 3 in c:
            checksum_threes += 1
    
    return checksum_threes * checksum_twos


with open("./input.txt") as input:
    all = [v.strip() for v in input.readlines()]
    all.sort()

    print("Checksum: {}".format(checksum(all)))

    a, b = find_off_by(1, all)
    final = "".join([a[i] for i in range(len(a)) if a[i] == b[i]])

    print("Matching id: ", final)


            
        
                

        
