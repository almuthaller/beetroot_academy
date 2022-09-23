# The greatest number

# Write a Python program to get the largest number from a list of random numbers with the length of 10

# Constraints: use only while loop and random module to generate numbers

import random


random_list = []

while len(random_list) < 10:
    random_list.append(random.randint(1,100))        # Random numbers between what range??

highest_number = max(random_list)

print(random_list)
print(f"The highest number in this list is {highest_number}.")
