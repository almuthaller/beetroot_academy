"""
Write a Python program to detect the number of local variables declared in a function.
"""

def a_function():
    a_variable = True
    another_variable = 2.5
    third_var, fourth_var = "3rd var", []


print(a_function.__code__.co_nlocals)