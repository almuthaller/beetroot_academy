# Just some practice for decorators


def memoize(func):
    memory = {}

    def wrapped_func(*args):
        if args not in memory:
            memory[args] = func(*args)
        else:
            print("I already know this one.")
        return memory[args]

    return wrapped_func


@memoize
def add(x, y):
    return x + y


print(add(3, 8))
print(add(5, 7))
print(add(3, 8))
