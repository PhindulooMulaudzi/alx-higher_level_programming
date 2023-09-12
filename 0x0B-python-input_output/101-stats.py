#!/usr/bin/python3

"""Module for stats."""

import sys


status = {}
size = 0
count = 0
for line in sys.stdin:
    split = line.split()
    status = split[-2]
    size += int(split[-1])
    if status in status.keys():
        status[status] += 1
    else:
        status[status] = 1
    count += 1
    if count == 10:
        sortme = sorted(status.keys())
        print("File size:", size)
        for keys in sortme:
            print("{}: {}".format(keys, status[keys]))
        count = 0
        continue
