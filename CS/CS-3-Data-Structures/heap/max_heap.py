class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        top = self.storage.pop(0)
        self.storage.insert(0, None)
        self._sift_down(0)
        return top

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return # nothing to bubble up, this is the 1st item
        parent_index = (index - 1) // 2
        if self.storage[parent_index] < self.storage[index] and index > 0:
            self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
            self._bubble_up(parent_index)
        

    def _sift_down(self, index):
        if self.get_size() < 2* index + 3: # if there's no children below this index
            self.storage.pop(index)
            if self.get_size() > 0: # If this is not the last index. Fill the 'hole'
                last = self.storage.pop(-1) # with the last element, otherwise, the array
                self.storage.insert(index,last) # may lose order
            return
        elif self.get_size() == 2 * index + 2:
            child_index = 2 * index + 1
        else:
            child_indices = [2 * index + 1, 2 * index + 2]
            if self.storage[child_indices[0]] > self.storage[child_indices[1]]:
                child_index = child_indices[0]
            else:
                child_index = child_indices[1]
        self.storage[index], self.storage[child_index] = self.storage[child_index],self.storage[index]
        self._sift_down(child_index)
