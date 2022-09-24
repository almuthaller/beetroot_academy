"""
The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:
"Hello <name>, on your next birthday you'll be <age+1> years"
"""

your_name = input("Hi! What's your name? ")
your_age = int(input("May I ask how old you are? "))  

print(f"Hello {your_name}, on your next birthday you'll be {your_age + 1} years old.")