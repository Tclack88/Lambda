class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        if comparator == None:
            self.comparator = lambda x, y: x > y
        else:
            self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        top = self.storage.pop(0)
        self.storage.insert(0, None)
        self._sift_down(0)
        return top

    def get_priority(self):
        return self.storage[0] # The top item, according to the comparator

    def get_size(self):
        return len(self.storage)

    ##### LEFT OFF HERE::: ####
    #### Problem with bubble up for deletion

    def _bubble_up(self, index):
        has_priority = False
        has_priority = self.comparator(self.storage[index], self.storage[(index - 1) //2])
        while has_priority and index > 0:
            parent_index = (index - 1) // 2
            child = self.storage[index]
            parent = self.storage.pop(parent_index)
            self.storage.insert(parent_index, child)
            self.storage.pop(index)
            self.storage.insert(index, parent)
            index = (index - 1) // 2
            has_priority = self.comparator(self.storage[index], self.storage[(index - 1) //2])


    def _sift_down(self, index):
        child_indices = 2 * index + 1, 2 * index + 2
        try:  # first check if both child indices exist
            if self.storage[child_indices[0]] and self.storage[child_indices[1]]:
                if self.comparator(self.storage[child_indices[0]], self.storage[child_indices[1]]):
                    child_index = child_indices[0]
                else:
                    child_index = child_indices[1]
            elif self.storage[child_indices[0]]: # if only one exists, it must be the 1st
                child_index = child_indices[0]
            else:
                self.storage.pop(index) # Otherwise, remove the element, you're likely
            child = self.storage[child_index]  # at the end
            self.storage[index] = child
            self.storage[child_index] = None
            self._sift_down(child_index)
        except IndexError:
            self.storage.pop(index)
            if len(self.storage) > 0: # if the list isn't empty, this exception occurs
                val_append = self.storage.pop(-1) # if there are no children for the
                self.storage.insert(index,val_append) # node, but there exist "lower tier"
                                         # values, so bring one up to avoid missing sift

# Eg. of final statement:
"""
        10                                  8
     8      5                           7      5
   6  7   1   2     -- remove 10 -->  6  ?   1   2 
  5                                  5 --^
"""

"""
heap = Heap(lambda x, y: x > y)

heap.insert(6)
heap.insert(7)
heap.insert(5)
heap.insert(8)
heap.insert(10)
heap.insert(1)
heap.insert(2)
heap.insert(5)

print(heap.storage)
"""
