# BinarySearchTree: A binary search tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_bst.py.
# YOUR NAME

class BinarySearchTree:

    def __init__(self, key = None):
        self.left = None
        self.right = None
        self.key = key

    def insert(self, node):
        if self.left:
            self.left.insert(node)
        elif node.key <= self.key:
            self.left = node
            self = node
        elif node.key >= self.key:
            self.right = node
            self = node

    
    def search(self, key):
        if key != self.key:
            return None
        elif self.key == key:
            return self
    
    def delete(self, key):
        if self.key != key:
            return self