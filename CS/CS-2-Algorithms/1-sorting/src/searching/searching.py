# STRETCH: implement Linear Search				
#arr = [0,1,2,3,4,5,6,7,8,9,10]
#target = 5
def linear_search(arr, target):
    for i, t in enumerate(arr):
        if t == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # array empty
      
    low = 0
    high = len(arr) - 1

    t = ''
    while t != target:
        middle = (high - low) // 2
        if arr[middle] == target:
            return middle
        elif target < middle:
            high = middle
        elif target > middle:
            low = middle 
    return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(arr)-1
    
    middle = (low + high) // 2

    if len(arr) == 0:
        return -1 # array empty
    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        high = middle
        return binary_search_recursive(arr, target, low, high)
    elif arr[middle] < target:
        low = middle
        return binary_search_recursive(arr, target, low, high)
    return -1 # not found
