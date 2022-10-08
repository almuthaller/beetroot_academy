"""
You need to transform the results of some function from an str type to an int type. Create a decorator for it. 
Advanced: create params for the decorator which will allow you to specify the final type.
"""

def convert_type(new_type):
    def arg_wrapper(func):
        def func_wrapper():
            result = new_type(func())
            return result
        return func_wrapper
    return arg_wrapper


@convert_type(float)
def testing():
    return "1"

print(type(testing()))