# We have a character and table 8 * 8. Randomly place on table some bombs. 
# User must input coordinates where character will go. 
# If user input a place with bomb - print "you loose". 
# If user will print twice in a row place without bomb - print "you win". 
# The total amount of bombs must be 18.

import random


bombs_placement = []

while len(bombs_placement) < 18:
    new_coordinates = random.randint(1, 8), random.randint(1, 8)
    if not new_coordinates in bombs_placement:
        bombs_placement.append(new_coordinates)


user_input = input("Guess coordinates: ").split(", ")

if not user_input in bombs_placement:
    user_input2 = input("Good! Guess new coordinates: ")
    if not user_input2 in bombs_placement:
        print("You win!")

else: 
    print("You loose.")
