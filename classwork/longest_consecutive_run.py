""" 
Write a function that takes on an input random ints (between 1 and 10) 
and returns the longest consecutive run and the length of that run of elements of the list.

Ex.     def task1(1,2,3,4,4,4,4,4,4,5,6,7,4,2,2,5) -> 6, 4
    def task1(1) -> 1, 1
    def task1() -> 0, None

Then create another function which takes on input result of function from the previous step 
and prints Informative message about the longest consecutive run, something like - “Longest run is 6 of integers - 4”
"""


def longest_run(*args):
    current_item = args[0]
    current_run = 1

    longest_item = None
    longest_run = 0

    for item in args[1:]:
        if current_item == item:
            current_run += 1
            if current_run > longest_run:
                longest_run = current_run
                longest_item = current_item

        else:
            current_item = item
            current_run = 1

    return (longest_run, longest_item)


print(longest_run(2, 3, 3, 3, 1, 2, 2, 2))
