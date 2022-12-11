"""
Implement your representation of Binary Search Tree. Your solution should contain classes for Node and Tree. 
Node only takes positive integers as values, able to store links to left and right children, and has str dunder method. 
Tree should support creation of object of that class, adding new Node to corresponding place in the existing Tree object 
(keep in mind that adding root Node will be a special case) and searching for Node with a given value. 
Search method of Tree class should return True if Node with that value exists and False otherwise.
"""


class Node:
    def __init__(self, value):
        if type(value) != int or value < 0:
            raise TypeError

        self.value = value
        self.right_child = None
        self.left_child = None

    def __str__(self):
        return str(self.value)


class Tree:
    def __init__(self):
        self.root = None

    def __insert_node(self, root, value):
        if root is not None:

            if value < root.value:
                if root.left_child is None:
                    root.left_child = Node(value)
                else:
                    self.__insert_node(root.left_child, value)

            elif value > root.value:
                if root.right_child is None:
                    root.right_child = Node(value)
                else:
                    self.__insert_node(root.right_child, value)

        else:
            self.root = Node(value)

    def add_node(self, value):
        self.__insert_node(self.root, value)

    def search_node(self, value):
        if type(value) != int or value < 0:
            raise TypeError

        current = self.root

        while current is not None:
            if value > current.value:
                current = current.right_child
            elif value < current.value:
                current = current.left_child
            else:
                return True

        return False

    def get_tree(self, root, tree=[]):
        if root is not None:
            self.get_tree(root.left_child, tree)
            tree.append(root.value)
            self.get_tree(root.right_child, tree)

        return tree

        # This method is not really usuable on its own unless root = self.root because argument root needs to be an instance of Node.
        # We do not store instances anywhere else because we create them directly in the add_node method of the class Tree.

    def print_all(self):
        print(self.get_tree(self.root))

    def find_min(self, root=None):
        if root is None:
            root = self.root

        if root.left_child is None:
            return root
        return self.find_min(root.left_child)

    def find_max(self, root=None):
        if root is None:
            root = self.root

        if root.right_child is None:
            return root
        return self.find_max(root.right_child)


tree = Tree()

assert tree.root is None

tree.add_node(5)

assert tree.root.value == 5

tree.add_node(14)
tree.add_node(3)
tree.add_node(1)
tree.add_node(7)
tree.add_node(5)

assert tree.root.value == 5

assert tree.search_node(5)
assert tree.search_node(14)
assert tree.search_node(3)
assert tree.search_node(1)
assert tree.search_node(7)

assert not tree.search_node(4)
assert not tree.search_node(15)

tree.print_all()

assert tree.find_min(), 1
assert tree.find_max(), 14
