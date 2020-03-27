from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item) # Add new item to head
            self.current = self.storage.head # put current at head
        else: # self.storage.length == self.capacity, so adding item would exceed capacity
            if self.current == self.storage.head: # If we're at the head...
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head.next # move "current" to 2nd item
            elif self.current == self.storage.tail: # If we're at the tail..
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.head
            else:
                self.current = self.current.next # advance current up
                self.current.insert_before(item) # add item before current
                self.current.prev.prev.delete() # delete the prev prev element

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        if self.storage.length > 0:
            present = self.storage.head
            list_buffer_contents.append(present.value)
            while present.next:
                present = present.next
                list_buffer_contents.append(present.value)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity # initialize blank list (test fails otherwise)
        self.current = None

    def append(self, item):
        if self.current == None: # after initial append
            self.current = 0 # Initialize 'current' pointer
        else:
            self.current = (self.current + 1) % self.capacity # modularly raise "current"
        self.storage.pop(self.current)
        self.storage.insert(self.current,item)

    def get(self):
        return [item for item in self.storage if item]
