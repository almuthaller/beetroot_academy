"""
Create a function where will be needed as an argument string_a and number_b. With using assert - be sure, that user input arguments of this types. After it concatenate string_a with number_b
"""

def my_function(string_a, number_b):
    assert type(string_a) == str, "first argument must be a string"
    assert type(number_b) == int, "second argument must be an int"

    return string_a + str(number_b)


print(my_function("a", 1))