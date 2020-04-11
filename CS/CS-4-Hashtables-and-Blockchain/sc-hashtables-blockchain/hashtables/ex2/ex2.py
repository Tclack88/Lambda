#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # overwrite route to be empty list
    route = []
    # create hash table linking source to destination
    for ticket in tickets: 
        hash_table_insert(hashtable,ticket.source, ticket.destination)

    # initialize next destination to be the value corresponding to "NONE" key
    next_destination = hash_table_retrieve(hashtable, 'NONE')
    while next_destination != 'NONE':
        # follow each key and add to route until next_destination = NONE (i.e. end)
        route.append(next_destination)
        next_destination = hash_table_retrieve(hashtable, next_destination)

    return route
