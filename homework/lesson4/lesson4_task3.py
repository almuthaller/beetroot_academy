# Words combination

# Create a program that reads an input string and then creates and prints 
# 5 random strings from characters of the input string.

# For example, the program obtained the word ‘hello’, 
# so it should print 5 random strings(words) that combine characters 'h', 'e', 'l', 'l', 'o' 
# -> 'hlelo', 'olelh', 'loleh' …

# Tips: Use random module to get random char from string)

import random 
given_string = input("Type something fun ")
list_of_char = list(given_string)
for i in range(5):
    random.shuffle(list_of_char)
    shuffled_string = ''.join(list_of_char)
    print(shuffled_string)