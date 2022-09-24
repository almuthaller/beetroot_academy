"""
Create “unwrap_maybe” function. It should take as first argument - list, for example [1, 2], and as second - index, for example 3. 
If index didn't exist in list, instead of exception - return a None object.
"""

def unwrap_maybe(my_list, my_index):
     if my_index >= len(my_list):
         return None
     return my_list[my_index]


print(unwrap_maybe([1,2,3,4], 3))