"""
Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""

def func1():
    print("You got me!")


def func2():
    return func1()


access_func1 = func2()