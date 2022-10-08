"""
String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. 
If the string length is less than 2, return instead of the empty string.
"""

input_string = input("Give me something fun to work with ")

# if len(input_string) < 2:
#     print("")
# else:
#     print(input_string[:2] + input_string[-2:])


# This code seems to work fine but it prints instead of returns. The output can't be used further.
# Attempt at definining a function that returns new string:


def make_weird_new_string(str):
    if len(str) < 2:
        return ""
    else:
        return str[:3] + str[-2:]


new_string = make_weird_new_string(input_string)

print(new_string)
