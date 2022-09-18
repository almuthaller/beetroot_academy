# Exclusive common numbers.

# Generate 2 lists with the length of 10 with random integers from 1 to 10, 
# and make a third list containing the common integers between the 2 initial lists without any duplicates.

# Constraints: use only while loop and random module to generate numbers

import random


first_list = []

while len(first_list) < 10:                     
    first_list.append(random.randint(1,10))

second_list = []

while len(second_list) < 10:        # Summarize and make a function so I don't have to copy code for the second list?
    second_list.append(random.randint(1,10))

common_integers = []  

for element in first_list:
    if element in second_list and not element in common_integers:
        common_integers.append(element)       

print(f"First list: {first_list}")
print(f"Second list: {second_list}")
print(f"The common elements are: {common_integers}")       