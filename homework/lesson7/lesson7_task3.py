# A simple calculator.

# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter 
# (to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) 
# as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. 
# For example:

#    the call make_operation('+', [7, 7, 2]) should return 16
#    the call make_operation('-', 5, 5, -10, -20) should return 30
#    the call make_operation('*', 7, 6) should return 42  

def make_operation(operator, numbers):
    
    if operator == "+":
        return sum(numbers)

    if operator == "-":
        result = numbers[0]
        for element in numbers[1:]:
            result -= element
        return result

    if operator == "*":
        result = numbers[0]
        for element in numbers[1:]:
            result *= element
        return result

# Some test cases:
assert make_operation("+", [2, 3, 4]) == 9
assert make_operation("-", [2, 3, 4]) == -5
assert make_operation("*", [2, 3, 4]) == 24


user_input = input("Numbers: ")
my_numbers = [int(x) for x in user_input.split(", ")]
my_operator = input("Operator: ")

my_result = make_operation(my_operator, my_numbers)

print(my_result)