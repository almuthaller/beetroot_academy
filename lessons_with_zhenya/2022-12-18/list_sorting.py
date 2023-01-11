def sort_list(_list):
    assert type(_list) == list

    if len(_list) < 2:
        return _list

    lower, equal, higher = [], [], []
    pivot = _list[0]

    for item in _list:
        if item < pivot:
            lower.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            higher.append(item)

    return sort_list(lower) + equal + sort_list(higher)


example_list = [16, 3, 9, 8, 23, 0]
assert sort_list(example_list) == sorted(example_list)
print(sort_list(example_list))
