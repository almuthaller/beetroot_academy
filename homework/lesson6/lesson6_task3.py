# List comprehension exercise

# Use a list comprehension to make a list containing tuples (i, j) 
# where i goes from 1 to 10 and j is corresponding to i squared.

list_i = []
i = 1
for what_should_i_name_this in range(10):
    list_i.append(i)
    i += 1
list_j = []
for element in list_i:
    list_j.append(element ** 2)
final_list = list(zip(list_i, list_j))
print(final_list)

# List comprehension!!