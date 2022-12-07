class Node:
    def __init__(self, value, next_node=None):
        if type(value) != int:
            raise TypeError
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class OrderedLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is not None:
            return_element = self.current
            self.current = self.current.next
            return return_element
        else:
            raise StopIteration

    def __str__(self):
        return str([x.value for x in self])

    def add_node(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        elif value < self.head.value:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            previous = None
            while current is not None:
                if current.next is None:
                    current.next = node
                    break
                if value < current.next.value:
                    node.next = current.next
                    current.next = node
                    break
                if value > current.next.value:
                    previous = current
                    current = current.next
                else:
                    break
            else:
                previous.next = node

    def __find_middle(self, first, last):
        if first is None:
            return None
        slow = first
        fast = first.next
        while fast != last:
            fast = fast.next
            if fast != last:
                slow = slow.next
                fast = fast.next
        return slow

    def binary_search(self, value):
        if type(value) != int:
            raise TypeError
        first = self.head
        last = None
        while True:
            middle = self.__find_middle(first, last)
            if middle is None:
                return False
            if middle.value == value:
                return True
            if middle.value < value:
                first = middle.next
            else:
                last = middle
            if last == first:
                break
        return False


our_list = OrderedLinkedList()

assert not our_list.binary_search(1)

our_list.add_node(1)
our_list.add_node(4)
our_list.add_node(2)
our_list.add_node(2)

assert str(our_list) == "[1, 2, 4]"

assert not our_list.binary_search(3)
assert not our_list.binary_search(0)
assert not our_list.binary_search(5)

assert our_list.binary_search(1)
assert our_list.binary_search(2)
assert our_list.binary_search(4)

our_list.add_node(6)

assert str(our_list) == "[1, 2, 4, 6]"

assert not our_list.binary_search(3)
assert not our_list.binary_search(0)
assert not our_list.binary_search(5)
assert not our_list.binary_search(7)

assert our_list.binary_search(1)
assert our_list.binary_search(2)
assert our_list.binary_search(4)
assert our_list.binary_search(6)
