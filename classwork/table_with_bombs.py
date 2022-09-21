# We have a character and table 8 * 8. Randomly place on table some bombs. 
# User must input coordinates where character will go. 
# If user input a place with bomb - print "you loose". 
# If user will print twice in a row place without bomb - print "you win". 
# The total amount of bombs must be 18.

import random


bombs_placement = set()

while len(bombs_placement) < 18:
    bombs_placement.add((random.randint(1, 8), random.randint(1, 8)))


user_input = input("Guess coordinates: ").split(", ")

if not user_input in bombs_placement:
    user_input2 = input("Good! Guess new coordinates: ")
    if not user_input2 in bombs_placement:
        print("You win!")

else: 
    print("You loose.")
