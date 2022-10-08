"""
You need a validation decorator, which will raise a Value error if one of the params of the function - will not be a string type. 
Advanced: add a parameter to decorator “searching_str”, this string must be in at least one argument of the wrapped function, 
or you should raise an error.
"""


def validation(searching_str):
    def arg_wrapper(func):
        def func_wrapper(*args):
            if any(type(argument) != str for argument in args):
                raise ValueError("One of your parameters is not a string.")
            assert searching_str in args, "Your given string is not an argument."
            return func(*args)

        return func_wrapper

    return arg_wrapper


@validation("test_string")
def test_function(*args):
    pass


test_function("string_arg", "test_string")
