"""
Create your own implementation of an iterable, which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax.
"""


class Iterable:
    def __init__(self, iterate_over):
        self.iterate_over = iterate_over

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        try:
            returned_value = self.iterate_over[self.current_index]
            # returned_value = self[self.current_index]             Question: which option do you prefer?
            self.current_index += 1
            return returned_value
        except IndexError:
            raise StopIteration

    def __getitem__(self, index):
        return self.iterate_over[index]


for e in Iterable("abcde"):
    print(e)

assert Iterable("abcde")[2] == "c"
assert Iterable([1, 4, 9, 2, 5, 14])[2] == 9
assert Iterable((4, 2, 8, 3, 1))[2] == 8
assert Iterable(range(5))[2] == 2
