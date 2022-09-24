"""
Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list 
that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration.
"""

integer_list = []

add_int = 1
while len(integer_list) < 100:
    integer_list.append(add_int)
    add_int += 1

new_list = []

for number in integer_list:                     #Use only while loop... does that apply here?
    if number % 7 == 0 and number % 5 != 0:
        new_list.append(number)

print(new_list)
