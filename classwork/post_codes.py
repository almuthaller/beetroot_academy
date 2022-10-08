"""
Create a function which will open a file by first argument (file_name), 
and will return first post-code in a file, which will contain the second argument (part_of_postcode_str)

for example:
Input: ("zip_codes.json", "36235")
Output: (["36235"])

Input: ("zip_codes.json", "36")
Output: (["36235", ...])

Advanced task: now, make it possible to put into a second argument a single value ("36235"), or a list of values (["36", "26"]). 
In a second case - function must return all post-codes that will suite at list one of the searching values
"""

import json


def find_zip_code(file_name, part_of_code):
    with open(file_name) as my_file:
        zip_codes = json.load(my_file)

        if type(part_of_code) == str:
            return [zip_code for zip_code in zip_codes if part_of_code in zip_code]

        elif type(part_of_code) == list:
            return set(zip_codes).intersection(set(part_of_code))


print(find_zip_code("classwork/zip_codes.json", "36"))
