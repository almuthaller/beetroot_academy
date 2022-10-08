"""
Play with lists/tuples using while loops

Find maximum from list of ints
Compute the average of tuple items
Reverse list using while loop
Copy items from one list to another
"""

my_list = [1, 6, 2, 3]
my_tuple = 2, 7, 4, 3, 3

# Task 1

maximum = max(my_list)

# print(maximum)


# Task 2

average = sum(my_tuple) / len(my_tuple)

# print(average)


# Task 3

reversed_list = []
index = len(my_list) - 1

while index >= 0:
    reversed_list.append(my_list[index])
    index -= 1

# print(reversed_list)


# Task 4

copied_list = []

for i in my_list:
    copied_list.append(i)

# print(copied_list)
