"""
Create your own implementation of a built-in function enumerate, named with_index(), which takes two parameters: 
iterable and start, default is 0. Tips: see the documentation for the enumerate function
"""


def with_index(iterable, start=0):
    for element in iterable:
        yield (start, element)
        start += 1


test_list = ["One", "Two", "Three", "One"]

print(list(with_index(test_list, 1)))
print(list(enumerate(test_list, 1)))
