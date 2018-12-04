#!/usr/bin/env python3

from collections import defaultdict
import re

with open("./input.txt") as input:
    events = sorted(input.readlines())

    sleepy_time = defaultdict(lambda: [0] * 60)
    guard = None
    for e in events:
        if "Guard" in e:
            guard = re.search('#(\d*)', e).group(1)
            asleep = None
        if "falls asleep" in e:
            asleep = int(re.search(':(\d*)]', e).group(1))
        if "wakes up" in e:
            awake = int(re.search(':(\d*)]', e).group(1))
            sleepy_time[guard][asleep:awake] = [v + 1 for v in sleepy_time[guard][asleep:awake]]
    
    strategy1 = sorted([(sum(v), k) for k,v in sleepy_time.items()], reverse=True)
    sleepiest = strategy1[0][1]
    sleepy_minutes = sleepy_time[sleepiest]
    sleepiest_minute = sleepy_minutes.index(max(sleepy_minutes))
    
    print("Guard #{} sleeps the most, mostly in minute {}".format(sleepiest, sleepiest_minute))
    print("Answer:", int(sleepiest) * sleepiest_minute)

    strategy2 = sorted([(max(v), k) for k,v in sleepy_time.items()], reverse=True)
    sleepiest = strategy2[0][1]
    sleepy_minutes = sleepy_time[sleepiest]
    sleepiest_minute = sleepy_minutes.index(max(sleepy_minutes))

    print("Guard #{} sleeps the most consistently in minute {}".format(sleepiest, sleepiest_minute))
    print("Answer:", int(sleepiest) * sleepiest_minute)