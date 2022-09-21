# We have a character and table 8 * 8. Randomly place on table some bombs. 
# User must input coordinates where character will go. 
# If user input a place with bomb - print "you loose". 
# If user will print twice in a row place without bomb - print "you win". 
# The total amount of bombs must be 18.

import random


def take_user_input(prompt):
    return tuple(input(prompt).split(", "))

bombs_placement = set()

while len(bombs_placement) < 18:
    bombs_placement.add((random.randint(1, 8), random.randint(1, 8)))


user_input = take_user_input("Guess coordinates: ")

if not user_input in bombs_placement:
    user_input2 = take_user_input("Good! Guess new coordinates: ")
  
if user_input in bombs_placement or user_input2 in bombs_placement:
    print("You loose.")
elif user_input == user_input2:
    print("You cheated >:( You loose.")
else:
    print("You win!")