class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def add_to_tail(self, value):
        new_node = Node(value)
        self.length += 1
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)
        self.length += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
        else:
            new_node.next = self.head
            self.head = new_node

    def contains(self, value):
        found = False
        current = self.head
        if current is None:
            return False
        while(not found):
            if current.value == value:
                found = True
            else:
                if current.next is None:
                    return found  # not found
                else:
                    current = current.next
        return found

    def get_max(self):
        completed = False
        max = 0
        current = self.head
        if current is None:
            return None
        while(not completed):
            if current.value > max:
                max = current.value
            if current.next is None or current == self.tail:
                completed = True
            current = current.next
        return max

    def remove_head(self):
        original_value = None
        if self.head is self.tail:  # one or fewer elements
            if self.head is None:  # list is empty
                return original_value
            else:  # only one element in list
                original_value = self.head.value
                self.head = None
                self.tail = None
                self.length = 0
        else:
            original_value = self.head.value
            self.head = self.head.next
            self.length -= 1

        return original_value

    def remove_tail(self):
        original_value = None
        if self.head is self.tail:  # one or fewer elements
            if self.tail is None:
                return original_value
            else:
                original_value = self.tail.value
                self.head = None
                self.tail = None
                self.length = 0
        else:
            current = self.head

            while (current.next is not self.tail):
                current = current.next

            original_value = self.tail.value
            self.tail = current
            self.tail.next = None

    def for_each(self, callback):
        pass


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
