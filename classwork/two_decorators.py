"""
Create a decorator for printing logs about when a function starts to run. 
After it - create a decorator which will convert the result of the function to some format, 
like “Result of function is {something}”. And put the function like “test_function_something” 
into two decorators in a row.

Example:
@log_decorator
@format_decorator
def some_function_test():
       pass
"""

from datetime import datetime


def log_decorator(func):
    def wraps(*args):
        print("Function started at: ", datetime.now())
        return func(*args)

    return wraps


def format_decorator(func):
    def wraps(*args):
        result = func(*args)
        return f"The result of the function is {result}"

    return wraps


@log_decorator
@format_decorator
def test_func():
    return 33


print(test_func())
