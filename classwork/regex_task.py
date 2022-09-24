"""
Write a program which will use regex to recognize if inputted by user number have a correct standard. 
References: +420 777 803 999, +1 203 532 345
If number is correct - print ("Good Number!"). If not - print "Wrong number format!"

Addition - modify this program to catch, was in a user input some number. 
If yes - parse it and print in output. If no - print "There is no number".
"""

from re import fullmatch, findall


valid_format = "\+[0-9]{1,3}\s\d{3}\s\d{3}\s\d{3}"      # Use https://regex101.com/ 

if fullmatch(valid_format, input("Phone number: ")):
    print("Valid phone number")
else:
    print("Invalid format")


# Addition:

is_phone_number = findall("\+[0-9]{1,3}\s\d{3}\s\d{3}\s\d{3}", input("Type phone number: "))

if is_phone_number:
    print(is_phone_number)
else:
    print("There is no number.")