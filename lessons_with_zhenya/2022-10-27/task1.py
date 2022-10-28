"""
Create a function that takes a list of integers as its argument and returns the biggest value from that list 
without using Python's built-in functions “min” and “max” or sorting the list.
"""


def find_biggest_value(list_of_ints):
    assert type(list_of_ints) == list
    biggest_value = list_of_ints[0]
    for element in list_of_ints[1:]:
        if element > biggest_value:
            biggest_value = element

    return biggest_value


print(find_biggest_value([5, 1, 2, 3, 8, 5]))
