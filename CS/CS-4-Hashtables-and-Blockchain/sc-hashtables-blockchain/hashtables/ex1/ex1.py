#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # create weight:index lookup table
    for i, w in enumerate(weights):
        hash_table_insert(ht, w, i)

    # Assuming only one viable pair,
    # check each weight for the existance of it's  "soul mate" <3
    for w in weights:
        if hash_table_retrieve(ht, limit - w):
            if w == limit - w: # edge case
                return [1,0]
            # if soul mate exists, find larger index and smaller index (via hash table)
            larger = max([hash_table_retrieve(ht, limit-w), hash_table_retrieve(ht,w)])
            smaller = min([hash_table_retrieve(ht, limit-w), hash_table_retrieve(ht,w)])
            return [larger, smaller]
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
