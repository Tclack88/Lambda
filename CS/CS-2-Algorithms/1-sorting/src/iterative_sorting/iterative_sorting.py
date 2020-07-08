# TO-DO: Complete the selection_sort() function below 

def selection_sort(arr):
    for i in range(len(arr)):   # for loop divides array into left (sorted) 
                                # and right(unsorted)
        smallest_of_arr = arr[i]
        curr_index = i  # must reset curr_index because "i" will shift while hunting
                        # for the smallest index in the while loop
        smallest_index = i
        while i < len(arr): # check the unsorted portion for the smallest number
                            # then bring that number to the appropriate spot
            if arr[i] < smallest_of_arr:
                smallest_of_arr = arr[i]
                smallest_index = i
            i += 1
        arr[curr_index], arr[smallest_index] = arr[smallest_index], arr[curr_index]
        #print(arr)
    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapping_occured = True
    while swapping_occured:
        swapping_occured = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapping_occured = True
        #print(arr)
    return(arr)


# STRETCH: implement the Count Sort function below
def count_sort(arr):
    arr_range = list(range(min(arr), max(arr) + 1))
    counts = [arr.count(x) for x in arr_range]
    cummulative_counts = [c + sum(counts[:i]) for i,c in enumerate(counts)]
    lte_map = dict(zip(arr_range, cummulative_counts))  # lte - less than or equal
                                                        # i.e. maps the count of numbers
                                                        # less than or equal to arr value
    arr_out = [0] * len(arr) # Prepopulate return array with 0 to handle missing vals
    for a in arr[::-1]: # strategy: return the last place each number will be found
        arr_out[lte_map[a] - 1]  = a # place last number based on cummulative counts
        lte_map[a] -= 1 # once number is placed, last number decrements
        #print(arr_out)
    return arr_out
