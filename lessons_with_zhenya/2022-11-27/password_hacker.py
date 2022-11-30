""" 
Use existing password generator function to generate passwords from 4 to 8 characters long that will contain only digits. 
Create a function that will try to guess generated password by brute force, e.g. continuously trying out all possible 
combinations of characters in the password. That mean that for only-digits password  of 4 characters length you potentially 
should try combinations from '0000', '0001', '0002' ... to ... '9999'. If guessed variant is equal to generated password 
- your brute force function will return its value. Then create (or find existing) time measurement decorator, decorate your 
brute force function with it and perform measurements of execution time for passwords of different length. Add results of 
measurements to your source file as a comment.
"""

from time import time
from random import randint


def password_generator(length):
    if type(length) != int:
        raise TypeError
    elif length < 4 or length > 8:
        raise ValueError

    password = ""
    for i in range(length):
        password += str(randint(0, 9))

    return password


def measure_execution_time(func):
    def wrap_function(*args):
        start_time = time()
        return_value = func(*args)
        print("Execution time: ", time() - start_time)
        return return_value

    return wrap_function


@measure_execution_time
def password_hacker(password):
    for length in range(4, 9):
        for guess in range(10**length):
            if str(guess).zfill(length) == password:
                return password


new_password = password_generator(7)
print(password_hacker(new_password))
# Execution time:  0.772s


# These are the longest possible execution times per password length:
password_hacker("9999")  # 0.001s
password_hacker("99999")  # 0.014s
password_hacker("999999")  # 0.145s
password_hacker("9999999")  # 1.462s
password_hacker("99999999")  # 14.783s

# The more times I run the programs the longer all the execution times become.
