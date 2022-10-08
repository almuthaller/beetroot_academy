"""
You have a list [1, 2, 3, 4, 5, 6, 7, 0]. 
Write a function "try_to_return_a_number", which will take an argument "number" 
and raise an exception OddError if number is odd, and ZeroError if number is zero. 
Write a high level function, which will take an argument "list_of_numbers", 
go through it in for in loop, put every item from list to "try_to_return_a_number" function, 
and print a number or a message depends on exception on each loop step.
"""


class OddError(Exception):
    pass


class ZeroError(Exception):
    pass


def try_to_return_a_number(number):
    if number % 2 != 0:
        raise OddError
    if number == 0:
        raise ZeroError
    return number


def high_level_function(list_of_numbers):
    for number in list_of_numbers:
        try:
            print(try_to_return_a_number(number))
        except OddError:
            print(f"{number} is an odd number")
        except ZeroError:
            print(f"{number} is a zero")


high_level_function([1, 2, 3, 4, 5, 6, 7, 0])
