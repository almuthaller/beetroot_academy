"""
You need to log the results of function sum(a, b) and function power(a, b) - to a file. 
+ Log each time when this function calls - another file, with a timestamp. Make a decorator for this one. 

Advanced: add parameters for a decorator, which will allow you to specify the names of a file.
"""

from datetime import datetime


def log_to_file(results_file_name, timestamps_file_name):
    def log_decorator(func):
        def wrap_func(*args):
            result = func(*args)
            with open(results_file_name, "a") as results_file:
                results_file.write(f"{func.__name__}: {result}\n")
            with open(timestamps_file_name, "a") as timestamps_file:
                timestamps_file.write(f"{func.__name__}: {datetime.now()}\n")
            return result
        return wrap_func
    return log_decorator


@log_to_file("classwork/results.txt", "classwork/timestamps.txt")
def sum(a, b):
    return a + b


@log_to_file("classwork/results.txt", "classwork/timestamps.txt")
def power(a, b):
    return a ** b


print(sum(2, 3))
print(power(2, 3))