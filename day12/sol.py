#!/usr/bin/env python3
from collections import defaultdict

def parseInitialState(line):
    state = []
    for c in line.replace("initial state: ", ""):
        state.append(c == '#')
    return state

def parseRule(line):
    test_state = [c == '#' for c in line[:5]]
    result = (line[-1] == '#')
    def rule(state):
        if state == test_state:
            return result
        return None
    return rule

def checkBounds(start_counter, state):
    if state[0]:
        state = [False, False, False,] + state
        start_counter -= 3
    elif state[1]:
        state = [False, False] + state
        start_counter -= 2
    elif state[2]:
        state = [False] + state
        start_counter -= 1

    if state[-1]:
        state = state + [False, False]
    elif state[-2]:
        state = state + [False]
    
    return start_counter, state

def generation(state, rules):
    new_state = [False, False]
    for x in range(2, len(state)-1):
        new_state.append(any(r(state[x-2:x+3]) for r in rules))
        
    return new_state + [False, False]

def sumPots(counter, state):
    total = 0
    for p in state:
        if p:
            total += counter
        counter += 1
    return total

def partOne(lines):
    counter, game_state = checkBounds(0, parseInitialState(lines[0]))
    rules = [parseRule(l.strip()) for l in lines[2:]]

    gen = 1
    gap = 0
    last_val = 0

    while True:
        counter, game_state = checkBounds(counter, generation(game_state, rules))
        val = sumPots(counter, game_state)
        diff = val - last_val
        if gen == 20:
            print("Sum of pots at :", gen, val)
        
        if diff == gap:
            print("Sum of pots at 50B :", val + (diff * (50000000000 - gen)))
            break
        
        gap = diff
        last_val = val
        gen += 1
        

with open('input.txt') as input:
    lines = input.readlines()

partOne(lines)
