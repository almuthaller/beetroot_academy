class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.prev = prev_node
        self.value = value
        self.next = next_node

    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current != self.tail:
            self.current = self.current.next
        else:
            raise StopIteration

    def add_tail_node(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def add_head_node(self, value):
        node = Node(value)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
