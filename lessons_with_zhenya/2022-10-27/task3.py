"""
Create a decorator for function. The decorator would print how long an invocation of a decorated function takes. 
Wrap the function from the previous task with this decorator.
"""

from time import time


def measure_execution_time(func):
    def wrap_function(*args):
        start_time = time()
        func(*args)
        print("Execution time: ", time() - start_time)
        return func(*args)

    return wrap_function


@measure_execution_time
def calculate_factorial(num):
    factorial = 1
    for number in range(1, num + 1):
        factorial *= number
    return factorial


print(calculate_factorial(5))
