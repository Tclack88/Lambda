from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10, hash_table = None):
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.hash_table = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.hash_table:
            node = self.hash_table.get(key)
            self.dll.move_to_front(node)
            return node.value 
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        node = self.hash_table.get(key) # returns None if not existant
        if node is not None:
            node.value = value
            self.dll.move_to_front(node) # If node already exists, move to head
            self.hash_table[key] = self.dll.head # update the key value pair
            return
        self.dll.add_to_head(value)
        self.hash_table[key] = self.dll.head # update hash table value if already exist
        if self.dll.length > self.limit:    # If we've added one too many, remove tail
            lru = self.dll.tail # lru = least recently used
            self.dll.remove_from_tail()
            deleted_key = [k for k,v in self.hash_table.items() if v == lru][0] 
            # key value pairs are unique in this case (because it's a memory address)
            # So getting that dictionary key that corresponds to the value, seems to be
            # the only way I can remove it from the hash table
            self.hash_table.__delitem__(deleted_key)    # why use 'pop' when something
        return                                          # more arcane exists

