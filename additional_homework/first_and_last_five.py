"""
Write a Python program to generate and print a list of first and last 5 elements 
where the values are square of numbers between 1 and 30 (both included).
"""

squared_numbers = [x ** 2 for x in range(1, 31)]
first_and_last_five = squared_numbers[:5] + squared_numbers[-5:]

print(first_and_last_five)


# Alternative solution:
numbers = list(range(1, 31))
first_and_last_five = [x ** 2 for x in numbers[:5] + numbers[-5:]]

print(first_and_last_five)
