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

    def add_node(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
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

    def __size(self, root=None):
        if root is None:
            return 0
        else:
            return self.__size(root.left_child) + 1 + self.__size(root.right_child)

    def size(self):
        return self.__size(self.root)

    def find_min(self):
        if self.root is None:
            return None

        root = self.root
        while root.left_child is not None:
            root = root.left_child

        return root.value

    def find_max(self):
        if self.root is None:
            return None

        root = self.root
        while root.right_child is not None:
            root = root.right_child

        return root.value

    def __walk(self, func, root):
        if root is not None:
            self.__walk(func, root.left_child)
            func(root.value)
            self.__walk(func, root.right_child)

    def walk(self, func):
        self.__walk(func, self.root)

    def to_list(self):
        result = []
        self.walk(result.append)
        return result

    def print_all(self):
        is_first = True

        def one_line_print(value):
            nonlocal is_first
            if not is_first:
                print(", ", end="")
            print(value, end="")
            is_first = False

        self.walk(one_line_print)
        print()


tree = Tree()

assert tree.root is None
assert tree.size() == 0

tree.add_node(5)

assert tree.root.value == 5
assert tree.size() == 1

tree.add_node(14)
tree.add_node(3)
tree.add_node(1)
tree.add_node(7)
tree.add_node(5)

assert tree.root.value == 5
assert tree.size() == 5

assert tree.search_node(5)
assert tree.search_node(14)
assert tree.search_node(3)
assert tree.search_node(1)
assert tree.search_node(7)

assert not tree.search_node(4)
assert not tree.search_node(15)

assert tree.to_list() == [1, 3, 5, 7, 14]
assert tree.size() == len(tree.to_list())

tree.print_all()

assert tree.find_min() == 1
assert tree.find_max() == 14
