"""
You have a first list like values = [“one”, “two”, “three”, “four”, “five”] and a second list indexes [1, 3, 5]. 
You need to remove elements from first list which have an indexes from a second.
"""

values = ["one", "two", "three", "four", "five", "six"]
indexes = [5, 1, 3]

indexes = list(set(indexes))

for item in reversed(indexes):
    values.pop(item)

print(values)