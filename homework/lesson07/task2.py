"""
Creating a dictionary.

Create a function called make_country, which takes in a country's name and capital as parameters. 
Then create a dictionary from those parameters, with 'name' and 'capital' as keys. 
Make the function print out the values of the dictionary to make sure that it works as intended.
"""

def make_country(country, capital):
    dictionary = {"Name": country, "Capital": capital}
    print(dictionary)

my_country = input("Some country name ")
my_capital = input("And the country's capital ")

make_country(my_country, my_capital)