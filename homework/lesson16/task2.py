"""
Create your own implementation of a built-in function range(), named in_range(), which takes three parameters: 
start, end, and optional step. Tips: See the documentation for range() function
"""


def in_range(start, end, step=1):
    while start < end:
        yield start
        start += step


for e in in_range(3, 13, 2):
    print(e)
