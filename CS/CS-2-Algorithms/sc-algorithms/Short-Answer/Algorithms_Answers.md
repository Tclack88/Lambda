#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n)

in this, `a` is essentially taking a step of n^2 until it gets to n^3. The sum of this is:

after the first loop a will be n^2, after the 2nd loop, 2n^2 ... etc., but the loop
is only n in length, each time a is incremented, it's one operation so this is

1 + 1 + 1 + .... + 1   <----- n times

= n

= O(n)


b) O(nlog(n))

summing step is a single operation. For each outer loop of i, the same number of operations are happening within the inner j loop. For each inner loop of j, j is incrementing the sum by 1, then 2 then 4 then 8 ... etc. until it incrememnts it by n (if it doesn't exceed it) But the sum of this is the same for each parent loop, so log\_2(n) operations occur
(e.g. if n = 32 then j takes on 1 -> 2 -> 4 -> 8 -> 16 -> 32. Each "arrow" here represent j changing, there are 5 changes which makes sense because log\_2(32) = 5.

Anyway, this occurs n times for the parent i loop, so n operations of log\_2(n) ~ nlogn

c) O(n)

for each n, the function calls itself until reaching 0, fortunately for this recursion, there's not multiple sub recursions happening, so it's easy to follow. So we must descend from n to 0 within the recursive loop. A final value is returned at some point (eventually returns 0) then we follow the series of returns back up from 0 to n. So in total 2n operations occur which is ~ O(n)

## Exercise II

Ignoring intuition (as in it's likely to be a *very* low floor since eggs are fragile thing) it's best to pretend this is an object with an unknown breaking point; it could very well be it breaks only from heights at or near the top. So let's treat this in the same manner as if someone told be to lookup a word in a Russian dictionary. Since I have no concept of character frequency, and I only know the order in which the characters appear the strategy would be the same: check in the middle. If it's not there, I check the middle of the upper half or lower half depending on whether I'm too high in the dictionary or too low. This is of course gonna be log(n) time if there are n words in the dictionary (as I described in problem I(b) above, so I will already build this on a **O(log(n))** time complexity. Here's the pseudo code:

```
def find_breaking_point(bottom, top):
    middle = n // 2
    if_egg_breaks_from_floor(n):
	top = n
        find_breaking_point(bottom, top)
    else:
        if top == botom:
            return top
        else:
            bottom = middle
	    find_breaking_point(bottom,top) 
```	

