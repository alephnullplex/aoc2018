#!/usr/bin/env python3

import re
from collections import defaultdict
from math import ceil

path = []
max_workers = 5
min_cost = 60
diff = ord('A')-1
infinite = 99999

def parseLine(line):
    # Pulls the two single capital letters into a tuple
    return re.search("\s([A-Z])\s.*\s([A-Z])\s", line).groups()

def requirementsMet(task_id, pre_reqs, c):
    if (task_id in path + tasks) or (c not in pre_reqs):
        return False # already seen it or not valid
    # check all requirements have already been met
    return all([(req in path) for req in pre_reqs])

def stepTime(step):
    return min_cost + (ord(step) - diff)

def newTime(worker, time):
    if worker[0] == infinite:
        return worker
    return (worker[0] - time, worker[1])

with open('./input.txt') as input:
    rules = [parseLine(l) for l in input.readlines()]

dag = defaultdict(list)
for r in rules:
    dag[r[1]].append(r[0])
    dag[r[0]] # make sure we create an empty list for all nodes

# start with the nodes that have no pre-reqs
tasks = sorted([k for k,v in dag.items() if v == []])    
while tasks:
    c = tasks[0]
    path.append(c)
    tasks = sorted(tasks[1:] + [k for k,v in dag.items() if requirementsMet(k, v, c)])

print("Sorted Instructions: ", "".join(path))

time = 0
# Use an infinite time for workers who are not busy to make sorting easier.
workers = [(infinite, None) for _  in range(max_workers)]

# start with the nodes that have no pre-reqs
tasks = sorted([k for k,v in dag.items() if v == []])    
path = []
while tasks or any(0 < w[0] < infinite for w in workers):
    available_workers = [w for w in workers if w[0] == infinite]
    busy_workers = [w for w in workers if w[0] != infinite]
    
    # assign tasks to workers
    span = min(len(tasks), len(available_workers))
    for i in range(span):
        available_workers[i] = (stepTime(tasks[i]), tasks[i])
    
    # remove the assigned tasks from the 'ready' list
    tasks = tasks[span:]
    workers = sorted(busy_workers + available_workers)

    # take the next complete task 
    completed = workers[0]
    this_time = completed[0]
    time += this_time
    # reduce all 'in progress' tasks by the time it took to complete this one
    workers = [newTime(w, this_time) for w in workers[1:]] + [(infinite, None)] # add the worker that just finished

    c = completed[1]
    path.append(c)
    tasks = sorted(tasks + [k for k,v in dag.items() if requirementsMet(k, v, c)])
    
print("Time to assemble:", time)



    

