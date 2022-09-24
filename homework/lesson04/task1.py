"""
The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
The result should be sent back to the user via a print statement.
"""

import random


random_number = random.randint(1,10)                                # I assume we're doing whole numbers??
guessed_number = int(input("Guess a whole number between 1 and 10 "))

if guessed_number == random_number:
    print("Yayyy, you guessed right! You win three washing machines.")
else:
    print(f"That's too bad. The number was {random_number}.")