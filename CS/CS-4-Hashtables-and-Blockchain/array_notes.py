class DynamicArray:
    def __init__(self, capacity=1):
        self.count = 0 # number of elements in the array
        self.capacity = capacity
        self.storage = [None] * capacity

    def insert(self, index, value):
        # Check if we have capacity
        # if not, add more
        if self.count >= self.capacity:
            self.resize()

        # shift over every item after index to the right by 1
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        # add new value to the index
        self.storage[index] = value
        # increment count
        self.count += 1 # the array is now one larger

    def append(self, value):
        # check if we have enough capacity, if not, resize
        if self.count >= self.capacity:
            self.resize()
        # Add value to the index of the count
        self.storage[self.count] = value
        self.count += 1

    def resize(self):
        # double capacity
        self.capacity *= 2
        # allocate a new storage array with double capacity
        new_storage = [None] * self.capacity
        # copy all elements from old storage to new
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage
        




a = DynamicArray(2)
a.insert(0,10)
a.insert(0,11)
print(a.storage)
a.append(9)
a.append(8)
print(a.storage)
a.append(7)
a.append('hello')
print(a.storage)


