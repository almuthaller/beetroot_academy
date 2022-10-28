"""
Create a function that takes a positive integer as its argument 
and returns the result of multiplication of all positive integers less or equal to the given one. 
For example, if argument is 5 return value will be equal to 120 (as result of calculation of the expression 1*2*3*4*5).

"""


def calculate_factorial(num):
    factorial = 1
    for number in range(1, num + 1):
        factorial *= number
    return factorial


print(calculate_factorial(5))
