#!/usr/bin/python

from collections import Counter
import sys
from math import ceil, factorial
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# OLD BAD ATTEMPT
# def eating_cookies(n, cache=None):
#     ways = 1
#     if n == 0:
#         return ways
#     for i in range(1, 4):
#         if n - i >= 0:
#             n -= i
#             ways += eating_cookies(n)
#         else:
#             break
#     return ways
def eating_cookies(n, cache=None):
    total_permutations = 0
    if n <=1 :
        return 1
    if n == 2:
        return 2
    for i in range(ceil(n / 3), n+1):
        # minimum sets of cookies eaten will be if all (or mostly) 3 at a time
        # maximum sets of cookies eaten will be 1 at a time
        # eg for 12 cookies it'll be [3,3,3,3] to [1,1,1,1,1,1,1,1,1,1,1,1,1]
        # no other sizes allowed
        check_list = [1] * i
        while sum(check_list) < n:
            # I begin with a list of n 1's in a list, then progressively increment
            # each until the sum of the list equals n (number of cookies)
            # eg. n = 6 [1,1,1,1] (not 7, continue)...
            #           [2,1,1,1] (not 7, continue)...
            #           [2,2,2,1] 7! (skipped previous, repetitive)
            check_list[check_list.index(min(check_list))] += 1
        cookie_counts = Counter(check_list)
        identical_cookies = [v for k,v in cookie_counts.items() if v > 1]
        permutations = factorial(len(check_list))
        for ic in identical_cookies:
            # calculate all the permutations, eg.
            # [2,2,2,1], [2,2,1,2], [2,1,2,2], [1,2,2,2]
            permutations = permutations // factorial(ic) # ensure integer div.
        total_permutations += permutations               # otherwise error from
        while cookie_counts[2] >= 2:                     # large number approx.
            # In some cases we will 1's and 1's or 2's and 3's
            # 2 2 2 2 2 1 1 1   or    3 3 3 2 2 2 2
            # We calculated the permutations for these above, but we will miss
            # some possibilities for this "size" of list
            # so if we have two 2's, we can remove them and add a 3 and 1
            # permutations of each of these will account for the remaining
            # posibilities
            cookie_counts.update({1:1, 2:-2, 3:1}) # lose two 2's, add 1 & 3
            check_list = list(cookie_counts.elements())
            identical_cookies = [v for k,v in cookie_counts.items() if v > 1]
            permutations = factorial(len(check_list))
            for ic in identical_cookies:
                permutations = permutations // factorial(ic)
            total_permutations += permutations

    return total_permutations


if __name__ == "__main__":
    if len(sys.argv) > 1:
      num_cookies = int(sys.argv[1])
      print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
      print('Usage: eating_cookies.py [num_cookies]')
