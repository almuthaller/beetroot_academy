# Write a Python program to create a list reflecting the run-length encoding from a given list of integers or characters.

# Original list:
# [1, 1, 2, 3, 4, 4.3, 5, 1]
# List reflecting the run-length encoding from the said list:
# [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]

# Original String:
# automatically
# List reflecting the run-length encoding from the said string:
# [[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]

original_list = [1, 1, 2, 3, 4, 4.3, 5, 1]
original_string = "automatically"

rle_list = []
count = 1
compare = ()

for element in original_list:       # Swap out original_list with original_string and the code will work the same.
    if compare == element:
        rle_list.pop()
        count += 1
    else:
        count = 1
    
    rle_list.append([count, element])
    compare = element


print(rle_list)