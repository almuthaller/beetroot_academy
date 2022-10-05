"""
Write a decorator arg_rules() that validates arguments passed to the function.

A decorator should take 3 arguments:

max_length: 15

type_: str

contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print the reason it failed; 
otherwise, return the result.

def arg_rules(type_: type, max_length: int, contains: list):
    pass


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
"""

def arg_rules(expected_type, max_length, contains):         # Never call your custom variables "type"! Baaaad idea.
    def args_wrapper(func):
        def func_wrapper(*args):
            for argument in args:
                try:
                    for argument in args:
                        assert type(argument) == expected_type, f"Expected type is {expected_type}, but we got: {type(argument)}"
                        assert len(argument) <= max_length, f"Maximum length should be {max_length}, but we got {len(argument)}."
                        assert all(symbol in argument for symbol in contains), f"Should contain: {contains}"
                except AssertionError as error:
                    print(str(error))
            return func(*args)
        return func_wrapper
    return args_wrapper


@arg_rules(expected_type=str, max_length=15, contains=['05', '@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("johndoe05@gmail.com") is False
assert create_slogan("S@SH05") == "S@SH05 drinks pepsi in his brand new BMW!"