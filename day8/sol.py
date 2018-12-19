#!/usr/bin/env python3

# s = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
# entries = list(map(int, s.split()))

with open('input.txt') as input:
    entries = list(map(int, input.read().split()))

def parseNode(e):
    child_count, meta_data_count, *e = e
    children = []
    for _ in range(child_count):
        child, e = parseNode(e)
        children.append(child)
    meta_data = e[:meta_data_count]
    e = e[meta_data_count:]
    return (children, meta_data), e

def sumMeta(tree):
    c, m = tree
    return sum(m) + sum(sumMeta(a) for a in c)

def sumValue(tree):
    c, m = tree
    lenc = len(c) + 1
    if lenc == 1:
        return sum(m)

    return sum(sumValue(c[i-1]) for i in m if i < lenc)

tree, _ = parseNode(entries)
print("Sum of metadata:", sumMeta(tree))
print("Value of tree:", sumValue(tree))
