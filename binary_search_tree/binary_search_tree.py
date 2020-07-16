"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)
        return

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # Inorder Traversal
    def in_order_print(self, node):
        # climb down left subtree
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        # climb down right subtree
        if node.right is not None:
            self.in_order_print(node.right)
        return

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            current = queue[0]
            print(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            queue.popleft()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)
        # climb down right subtree
        if node.right is not None:
            self.dft_print(node.right)
        # climb down left subtree
        if node.left is not None:
            self.dft_print(node.left)
        return

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # print root
        print(node.value)
        # climb down left subtree
        if node.left is not None:
            self.pre_order_dft(node.left)
        # climb down right subtree
        if node.right is not None:
            self.pre_order_dft(node.right)
        return

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # climb down left subtree
        if node.left is not None:
            self.post_order_dft(node.left)
        # climb down right subtree
        if node.right is not None:
            self.post_order_dft(node.right)
        # print root
        print(node.value)
        return
