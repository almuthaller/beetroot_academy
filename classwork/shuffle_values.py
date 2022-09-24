"""
Create list which will have 1000000 sorted numbers. After it, create a copy of this list and shuffle
the values. After it, filter all odd elements, and measure, how much time it'll take for sorted and unsorted list.
"""

from random import shuffle

from copy import deepcopy

from time import time


todays_list = list(range(1000000))

copied_list = deepcopy(todays_list)

shuffle(copied_list)

time_start = time()

odd_elemnts = [x for x in todays_list if x % 2]

print("Sorted list: ", time() - time_start)

time_start2 = time()

odd_elements_from_shuffled = [x for x in copied_list if x % 2]

print("Shuffled list: ", time() - time_start2)