class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        print('inserting....',value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        self.storage[0] = None
        self._sift_down(0)

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        print('bubble up')
        print(self.storage)
        if index == 0:
            return # nothing to bubble up, this is the 1st item
        parent_index = (index - 1) // 2
        if self.storage[parent_index] < self.storage[index] and index > 0:
            self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
            self._bubble_up(parent_index)
        

    def _sift_down(self, index):
        print('sifting down')
        if self.get_size() < 2* index + 2:
            self.storage.pop(index)
            return
        elif self.get_size() < 2 * index + 2:
            child_index = 2 * index + 1
        else:
            child_indices = [2 * index + 1, 2 * index + 2]
            if self.storage[child_indices[0]] > self.storage[child_indices[1]]:
                child_index = child_indices[0]
            else:
                child_index = child_indices[1]
        self.storage[index], self.storage[child_index] = self.storage[child_index],self.storage[index]
        self._sift_down(child_index)
        print(self.storage)   
