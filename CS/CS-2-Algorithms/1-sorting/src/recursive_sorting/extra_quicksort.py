#!/usr/bin/env python3

from random import seed, shuffle
seed(5)
arr = [0,1,2,3,5,8,13,21,34]
shuffle(arr)
#print(arr)


def quick_sort(arr):
    array_sorted = True
    for i in range(len(arr)):
        if arr[i-1] > arr[i]:
            array_sorted = False
    if array_sorted:
        return arr
    pivot = 0 # random is a better choice
    unsorted = arr[pivot:]
    smaller = [i for i in unsorted if i < arr[pivot]]
    larger = [i for i in unsorted if i > arr[pivot]]
    return quick_sort(smaller) + [arr[pivot]] + quick_sort(larger)


#print(quick_sort(arr))

