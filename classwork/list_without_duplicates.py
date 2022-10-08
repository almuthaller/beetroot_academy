"""
Create a function that takes on an input random ints (between 1 and 10) and returns the list, without duplicates. 
Try to create two versions of this function - first with usage set and list constructors and second only using for-in loops.
"""


def erase_duplicates(*args):
    return list(set(args))


print(erase_duplicates(1, 3, 3, 2, 4))


def erase_duplicates_2(*args):
    list_without_duplicates = []
    for argument in args:
        if not argument in list_without_duplicates:
            list_without_duplicates.append(argument)

    return list_without_duplicates


print(erase_duplicates_2(1, 3, 3, 2, 4))
