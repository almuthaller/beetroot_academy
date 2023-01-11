# Binary search using recursion


def binary_search(sequence, value, low, high):
    if low > high:
        return None
    middle = (high + low) // 2
    middle_value = sequence[middle]
    if middle_value == value:
        return middle
    elif middle_value < value:
        return binary_search(sequence, value, middle + 1, high)
    else:
        return binary_search(sequence, value, low, middle - 1)


def search(sequence, value):
    assert type(sequence) == list
    assert sequence == sorted(sequence)
    return binary_search(sequence, value, 0, len(sequence) - 1)


print(search([1, 2, 3, 5, 6, 7], 5))
