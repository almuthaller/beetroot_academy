"""
Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
"""

some_lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

highest_sum = 0

for sublist in some_lists:
    if sum(sublist) > highest_sum:
        highest_sum = sum(sublist)
        print_list = sublist

print(print_list)