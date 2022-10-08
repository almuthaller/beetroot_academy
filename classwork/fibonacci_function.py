"""
Create a fibonacci function, which will take from user input - number index in the sequence and will print a number under this index.
https://en.wikipedia.org/wiki/Fibonacci_number
"""


def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)
