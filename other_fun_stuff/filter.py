# Just some practice as a pre-stage for decorators

def filter(list, func):
    return [element for element in list if func(element)]

my_list = [1, 2, 3, 4, 5, 6, 7]

def is_odd(number):
    return (number % 2 != 0)

print(filter(my_list, is_odd))