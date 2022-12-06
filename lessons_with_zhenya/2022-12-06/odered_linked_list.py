class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return self.value


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
                elif value < current.next.value:
                    node.next = current.next
                    current.next = node
                    break
                elif value > current.next.value:
                    previous = current
                    current = current.next
                else:
                    break
            else:
                previous.next = node
                node.next = None

    def binary_search(self):
        pass


our_list = OrderedLinkedList()
our_list.add_node(1)
our_list.add_node(4)
our_list.add_node(2)
our_list.add_node(2)
for i in our_list:
    print(i.value)
