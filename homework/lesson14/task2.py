"""
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):
    pass


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
"""


def stop_words(words):  # Decorator with arguments --> make two nested decorators
    def args_wrapper(func):
        def func_wrapper(*args):
            returned_str = func(*args)
            for word in words:
                returned_str = returned_str.replace(word, "*")
            return returned_str

        return func_wrapper

    return args_wrapper


@stop_words(["pepsi", "BMW"])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


@stop_words(["blue", "green", "yellow"])
def concatenate(*strings):
    return " ".join(strings)


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
assert (
    concatenate("Almut", "Papa is always blue", "Grossschaf")
    == "Almut Papa is always * Grossschaf"
)
