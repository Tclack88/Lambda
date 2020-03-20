'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    if len(word) <=1 :
        return 0
    front = word[:-1]
    back = word[-1]
    if front[-1] + back == 'th':
        return 1 + count_th(front)
    else:
        return count_th(front)
