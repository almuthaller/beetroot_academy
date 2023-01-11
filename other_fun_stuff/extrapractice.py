"""
Write a function "search" that takes a list and a value to search for,
and returns the first index of the value in the list if found, or None if not.

The list is required to be sorted on input; you might assert this at the
beginning of the function.

Write unit tests for the function; try to cover as many interesting edge cases
as you can think of.

Measure the time it takes to call the function (using time.time()), e.g. for
cases like

  my_list = list(range(100000))
  index = search(my_list, 80000)

Now, reimplement the function using a binary search algorithm. (Look it up on
Wikipedia to find out what this is.) Use your existing tests to verify that the
new implementation works the same as the old one.

Measure the time again, as above.
"""

import time


def search(search_in, search_for):
    start = time.time()
    assert type(search_in) == list, "First argument must be a list."
    assert search_in == sorted(search_in), "Your input list must be sorted."
    try:
        return search_in.index(search_for)
    except ValueError:
        return None
    finally:
        end = time.time()
        print(f"Measured execution time: {end - start}")


def binary_search(search_in, search_for):
    start = time.time()
    assert type(search_in) == list, "First argument must be a list."
    assert search_in == sorted(search_in), "Your input list must be sorted."
    first_index = 0
    last_index = len(search_in) - 1
    found_index = None
    while first_index <= last_index:
        middle = (first_index + last_index) // 2
        if search_in[middle] > search_for:
            last_index = middle - 1
        elif search_in[middle] < search_for:
            first_index = middle + 1
        else:
            found_index = middle
            while found_index > 0 and search_in[found_index - 1] == search_for:
                found_index -= 1
            break

    end = time.time()
    print(f"Measured execution time: {end - start}")
    return found_index


if __name__ == "__main__":
    print("Search:")
    print(search(list(range(100000)), 50000000))

    print("Binary search:")
    print(binary_search(list(range(100000)), 50000000))

    """
    for n in range(100):
        if search(list(range(100)), n) != n:
            print(f"search() does not work for {n}")

    for n in range(100):
        if binary_search(list(range(100)), n) != n:
            print(f"binary_search() does not work for {n}")
    """

    # Wo im Code schreibe ich die Tests hin?
    # warum:
    # if __name__ == '__main__':
    #    unittest.main()
