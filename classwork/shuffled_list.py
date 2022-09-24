"""
Create function which will shuffle a given list of items and return a shuffled list.
Do not use the shuffle() method.
"""

import random


def shuffle_list(given_list):
    shuffled_list = []
    used_indexes = []
    
    while len(shuffled_list) < len(given_list):
        random_index = random.randint(0, len(given_list) - 1)

        if not random_index in used_indexes:
            shuffled_list.append(given_list[random_index])
            used_indexes.append(random_index)
    
    return shuffled_list


my_list = [1, 2, 3]

print(shuffle_list(my_list))