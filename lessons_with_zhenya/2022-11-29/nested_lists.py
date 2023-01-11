# Find the maximum integer in a list of nested lists

example_list = [3, 4, [5, 2, 1, [23, 9], 8], [4, 87], 17, 16, [3, 5, [[34]]]]


def find_max(nested_list):
    max = 0  # Working with postive ints only for now
    for element in nested_list:
        if type(element) == int:
            if element > max:
                max = element
        elif type(element) == list:
            temporary_max = find_max(element)
            if temporary_max > max:
                max = temporary_max

    return max


print(find_max(example_list))
