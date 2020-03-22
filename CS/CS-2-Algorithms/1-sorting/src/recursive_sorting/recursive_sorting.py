# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    for i in range(elements):
        if len(arrA) == 0 or len(arrB) == 0:
            break
        elif arrA[0] < arrB[0]:
            transfer = arrA.pop(0)
        else:
            transfer = arrB.pop(0)
        merged_arr[i] = transfer
        #print(merged_arr)
    tail = arrA + arrB  # group what's left (an empty list and a sorted list)
    merged_arr[-1* len(tail):] = tail # change final zeros to the tail
    #print(merged_arr)
    return merged_arr

# Ignore this trash
# def merge_sort(arr):
#     sorted_arr = []
#     if arr == sorted_arr: # if arr is empty list, no sorting needed
#         return sorted_arr
#     if type(arr[0]) != list:
#         arr = [[elem] for elem in arr]
#     for i in range(0, len(arr), 2):
#         try:
#             sorted_arr.append(merge(arr[i],arr[i+1]))
#         except IndexError:
#             sorted_arr.append(arr[i])
#             if len(sorted_arr) > 1:
#                 continue
#             else:
#                 return sorted_arr[0]
#     sorted_arr = merge_sort(sorted_arr)
#     return sorted_arr

# Much Cleaner
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        return merge(merge_sort(left), merge_sort(right))
    return arr


# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO
# 
#     return arr
# 
# def merge_sort_in_place(arr, l, r): 
#     # TO-DO
# 
#     return arr

def merge_in_place( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    for i in range(elements):
        if len(arrA) == 0 or len(arrB) == 0:
            break
        elif arrA[0] < arrB[0]:
            transfer = arrA.pop(0)
        else:
            transfer = arrB.pop(0)
        merged_arr[i] = transfer
        #print(merged_arr)
    tail = arrA + arrB  # group what's left (an empty list and a sorted list)
    merged_arr[-1* len(tail):] = tail # change final zeros to the tail
    print(merged_arr)
    return merged_arr

def merge_sort_in_place( arr ):
    if arr == []: # if arr is empty list, no sorting needed
        return arr
    is_sorted = False
    while not is_sorted:
        sorted_arr = [] # Set a blank array to be used for next loop
        is_sorted = True
        if type(arr[0]) == list:
            merged_arr = [item for sublist in arr for item in sublist]
        else:
            merged_arr = arr
        for i in range(len(merged_arr)): # check if sorted based on relative values
            if i == 0: # skip 0th case, otherwise it's checked with the -1 element
                continue
            if merged_arr[i-1] > merged_arr[i]:
                is_sorted = False
        if is_sorted: # leave while loop before the rest of this happens
            continue
        if type(arr[0]) != list: # convert initial array into list
            arr = [[elem] for elem in arr]
        for i in range(0, len(arr), 2):
            try:
                sorted_arr.append(merge_in_place(arr[i],arr[i+1]))
            except IndexError:
                sorted_arr.append(arr[i])
        arr = sorted_arr
    return arr[0]

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def insertion_sort(arr):
    for i in range(len(arr)):
        while arr[i] < arr[i-1] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
            #print(arr) # check after each insertion
    return arr


def timsort(arr):
    if len(arr) > 64:
        left = timsort(arr[:len(arr)//2])
        right = timsort(arr[len(arr)//2:])
        return just_merge(insertion_sort(left),insertion_sort(right))
    else:
        return just_merge(insertion_sort(arr[:len(arr)//2]),insertion_sort(arr[len(arr)//2:]))

def just_merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    for i in range(elements):
        if len(arrA) == 0 or len(arrB) == 0:
            break
        elif arrA[0] < arrB[0]:
            transfer = arrA.pop(0)
        else:
            transfer = arrB.pop(0)
        merged_arr.append(transfer)
        #print(merged_arr)
    tail = arrA + arrB  # group what's left (an empty list and a sorted list)
    merged_arr.extend(tail) # change final zeros to the tail
    #print(merged_arr)
    return merged_arr
