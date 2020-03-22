#!/usr/bin/env python3

from robot_sort import SortingRobot as Robot1
from robot_sort2 import SortingRobot as Robot2
from random import seed, sample

seed(5)





lists = []

for i in range(100):
    lists.append(sample(range(300),100))

r1time = 0
r2time = 0
for l in lists:
    r1 = Robot1(l)
    r2 = Robot2(l)
    t1 = r1.sort()
    t2 = r2.sort()
    r1time += t1
    r2time += t2

print('Robot 1 time:', r1time)
print('Robot 2 time:', r2time)

print(f'Robot 1 is {round(t1time/r2time)} times faster than Robot2')
