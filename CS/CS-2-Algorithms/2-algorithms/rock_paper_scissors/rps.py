#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    combinations = []
    rps_map = {'0':'rock', '1':'paper', '2':'scissors'}
    if n == 0:
        return [[]]
    elif n == 1:
        return [['rock'],['paper'],['scissors']]
    for i in range(3**n):   # 3 possibilities: rock, paper scissors
        if i == 0:              # and for n throws, there will be 3^n outputs
            element = '0'.zfill(n) # return string front filled with n 0's
            combinations.append([rps_map[x] for x in list(element)])
                            # map number to rock, paper or scisssors
        else: # convert i to base 3 string and repeat the above procedure
            nums = []
            while i:
                i, r = divmod(i, 3) # i, r is integer div, remainder
                                    # e.g. divmod(7,3) = 2,1
                nums.insert(0,(str(r))) # add to front of list
            element = ''.join(nums).zfill(n)
            combinations.append([rps_map[x] for x in list(element)])

    return combinations

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
