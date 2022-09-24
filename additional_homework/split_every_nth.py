"""
Write a Python program to split a list every Nth element.
Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""

def split_list(given_list, n):
    final_lists = []

    for i in range(n):
        add_list = given_list[i::n]
        final_lists.append(add_list)

    return final_lists


print(split_list([1, 2, 3, 4, 5, 6, 7, 8], 3))
