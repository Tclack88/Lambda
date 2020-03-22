#!/usr/bin/env python3

from recursive_sorting.recursive_sorting import merge, merge_sort, insertion_sort, timsort, just_merge
from recursive_sorting.extra_quicksort import quick_sort
from iterative_sorting.iterative_sorting import selection_sort, bubble_sort, count_sort

from random import sample, seed
from time import perf_counter as pc
seed(5)
lists = []

for i in range(20):
    lists.append(sample(range(2000),2000))

print("Sort Comparison Tests\n(sorting 20 lists 2000 in length each)\n\n")

print("::: Iterative Sorting Methods :::")

print("\nSelection Sort")
start = pc()
for l in lists:
    a = l.copy()
    selection_sort(a)
stop = pc()
print('Time')
print(stop - start)

print("\nBubble Sort")
start = pc()
for l in lists:
    a = l.copy()
    bubble_sort(a)
stop = pc()
print('Time')
print(stop - start)

print("\nCount Sort")
start = pc()
for l in lists:
    a = l.copy()
    count_sort(a)
stop = pc()
print('Time')
print(stop - start)


print("::: Recursive Sorting Methods::: ")

print('\nQuick Sort')
start = pc()
for l in lists:
    a = l.copy()
    quick_sort(a)
stop = pc()
print('Time')
print(stop - start)


print('\nInsertion sort')
start = pc()
for l in lists:
    a = l.copy()
    insertion_sort(a)
stop = pc()
print('Time')
print(stop - start)

print("\nMerge Sort")
start = pc()
for l in lists:
    a = l.copy()
    merge_sort(a)
stop = pc()
print('Time')
print(stop - start)


print("\nTimsort")
start = pc()
loop = 0
for l in lists:
    loop += 1
    a = l.copy()
    timsort(a)
stop = pc()
print('Time')
print(stop - start)



