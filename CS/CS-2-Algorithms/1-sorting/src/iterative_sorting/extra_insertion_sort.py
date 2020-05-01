#!/usr/bin/env python3

arr = [6, 4, 2, 1, 8, 11, 0, 5]

print("Start:\n  ",arr)

def insertion_sort(arr):
    for i in range(len(arr)):
        while arr[i] < arr[i-1] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
            print(arr) # check after each insertion
    return arr


print('### insertion sort ###')
print('sorted:', insertion_sort(arr))

# everything below is shown in assignments, so nothing new 
"""
arr = [6, 4, 2, 1, 8, 11, 0, 5]
print("Start:\n  ",arr)

def selection_sort(arr):
    for i in range(len(arr)):
        smallest_of_arr = arr[i]
        current_index = i
        smallest_index = i
        while i < len(arr):
            if arr[i] < smallest_of_arr:
                smallest_of_arr = arr[i]
                smallest_index = i
            i += 1
        arr[current_index], arr[smallest_index] = arr[smallest_index], arr[current_index]
        print(arr)
    return arr


print('### selection sort ###')        
print('sorted:', selection_sort(arr))



arr = [6, 4, 2, 1, 8, 11, 0, 5]
print("Start:\n  ",arr)

def bubble_sort(arr):
    swapping_occured = True
    while swapping_occured:
        swapping_occured = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapping_occured = True
        print(arr)
    return(arr)

print('### bubble sort ###')
print('sorted:', bubble_sort(arr))


print('\n### count sort ###')
arr = [6, 4, 2, 1, 8, 11, 0, 5]
print("Start:\n  ",arr)
def count_sort(arr):
    arr_range = list(range(min(arr), max(arr) + 1))
    counts = [arr.count(x) for x in arr_range]
    cummulative_counts = [c + sum(counts[:i]) for i,c in enumerate(counts)]
    lte_map = dict(zip(arr_range, cummulative_counts))  # lte - less than or equal
                                                        # i.e. maps the count of numbers
                                                        # less than or equal to each key
    arr_out = [0] * len(arr) # Prepopulate return array with 0 to handle missing vals
    for a in arr[::-1]: # strategy, return the last place each number will be found
        arr_out[lte_map[a] - 1]  = a # place last number based on cummulative counts
        lte_map[a] -= 1 # once number is placed, last number decrements
        print(arr_out)
    return arr_out

print('sorted:', count_sort(arr))
"""
