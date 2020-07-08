# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.count = 0 # keep track of number of items
        self.upper_load_factor = .7
        self.lower_load_factor = .2
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return self._hash_djb2(key)#hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # Take starting number, shift left by 5 bytes, add to that the original number
        # add the first character of the key (byte char). Repeat until all chars used
        byte_key = bytes(key, encoding='ascii')
        hashed_key = 5381 # commonly chosen "arbitrary large prime"
        for b in byte_key:
            hashed_key = (hashed_key << 5) + hashed_key + b
        return hashed_key


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        self.count += 1
        if self.count / self.capacity > self.upper_load_factor:
            print("RESIZE CALLED")
            self.resize('up')

        index = self._hash_mod(key) #self._hash(key) % self.capacity
        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key,value)
        else:
            # add new pair to existing index entry (old pair)
            old_pair = self.storage[index]
            new_pair = LinkedPair(key,value)
            new_pair.next = old_pair
            self.storage[index] = new_pair



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key) #self._hash(key) % self.capacity
        if self.storage[index] == None:
            print(f'key: "{key}" not found')
        else:
            self.storage[index] = None  
            #TODO: deal with linked pairs under same hash
        self.count -= 1
        if self.count / self.capacity < self.lower_load_factor:
            print('resizing down!')
            self.resize('down')


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key) #self._hash(key) % self.capacity
        if self.storage[index] == None:
            return None
        else:
            item = self.storage[index]
            while True:
                if item.key == key: # check if key is this item, return value if true
                    return item.value
                if item.next == None: # break out if there's no next item
                    return None
                item = item.next # if next item exists, recheck loop
                



    def resize(self, direction='up'):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage # make copy of old storage

        if direction == 'up':
            self.capacity *= 2 # double the allowed capacity
        elif direction == 'down' and self.capacity > 8:
            self.capacity //= 2
        else:
            print("Not going lower than 8")
            return

        new_storage = [None] * self.capacity
        self.storage = new_storage
        for item in old_storage:
            if item != None:
                # All objects in linked list would have the same mod because
                # they share the same hash. So the whole object, chained or not
                # can be moved to the index (which is the same as that of the 1st item)
                linked_pairs = []
                while item.next != None: # check for item.next's insert into new array
                    next_item = item.next
                    item.next = None
                    linked_pairs.append(item)
                    self.insert(item.key, item.value)
                    self.count -= 1
                    item = next_item
                # insert first and only item if while loop is skipped
                # other wise add last item in while loop
                self.count -= 1
                self.insert(item.key, item.value)
        print('storage after resize:', len(self.storage))
            


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
