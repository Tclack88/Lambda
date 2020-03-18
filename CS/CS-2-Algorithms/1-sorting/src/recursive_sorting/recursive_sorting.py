# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
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
    #print(merged_arr)
    return merged_arr


def merge_sort( arr ):
    sorted_arr = []
    if arr == sorted_arr: # if arr is empty list, no sorting needed
        return sorted_arr
    if type(arr[0]) != list:
        arr = [[elem] for elem in arr]
    for i in range(0, len(arr), 2):
        try:
            sorted_arr.append(merge(arr[i],arr[i+1]))
        except IndexError:
            sorted_arr.append(arr[i])
            if len(sorted_arr) > 1:
                continue
            else:
                return sorted_arr[0]
    sorted_arr = merge_sort(sorted_arr)
    return sorted_arr


#print(merge_sort(arr))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
