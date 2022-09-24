"""
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys 
and the number of occurrences as values. 
"""

sentence = input("Type a sentence without punctuation :) ")     # How would we solve it if there was punctuation in the input?
keys = sentence.lower().split()

# values = []

# for element in keys:
#     element_count = keys.count(element)
#     values.append(element_count)

# our_dictionary = dict(zip(keys, values))

# print(our_dictionary)


our_dictionary = {}

for element in keys:
    if element in our_dictionary:
        our_dictionary[element] += 1
    else: 
        our_dictionary[element] = 1

print(our_dictionary)