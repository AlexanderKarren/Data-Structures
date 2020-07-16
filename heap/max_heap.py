class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        index = len(self.storage) - 1
        parent = int((index - 1) / 2)
        # while value is greater than its parent
        while self.storage[index] > self.storage[parent]:
            temp = self.storage[parent]
            self.storage[parent] = self.storage[index]
            self.storage[index] = temp

    def delete(self):
        temp = self.storage[0]
        leaf_index = len(self.storage) - 1
        self.storage[0] = self.storage[leaf_index]
        self.storage[leaf_index] = temp
        self.storage.pop()
        index = 0
        right_value = self.storage[(2 * index) + 2]
        left_value = self.storage[(2 * index) + 1]
        value = self.storage[index]
        while value < right_value or value < left_value:
            print("did this")
            index = self._sift_down(index)

    def get_max(self):
        return self.storage[0] if self.storage[0] else None

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        right_index = (2 * index) + 2
        left_index = (2 * index) + 1
        temp = self.storage[index]
        # print("debug:", len(self.storage), right_index, left_index)
        # if left child is greater than / equal to right child
        if self.storage[left_index] >= self.storage[right_index]:
            self.storage[index] = self.storage[left_index]
            self.storage[left_index] = temp
            return left_index
        else:
            self.storage[index] = self.storage[right_index]
            self.storage[right_index] = temp
            return right_index

# i left = 2i + 1
# i right = 2i + 2
# i parent = (i - 1) / 2
