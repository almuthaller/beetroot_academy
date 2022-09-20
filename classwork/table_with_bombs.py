# We have a character and table 8 * 8. Randomly place on table some bombs. 
# User must input coordinates where character will go. 
# If user input a place with bomb - print "you loose". 
# If user will print twice in a row place without bomb - print "you win". 
# The total amount of bombs must be 18.

import random


bombs_placement = []

for i in range(18):
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    new_coordinates = x, y
    if not new_coordinates in bombs_placement:
        bombs_placement.append(new_coordinates)


user_input = input("Guess coordinates: ").split(", ")

if user_input in bombs_placement:
    user_input2 = input("Hit! Guess new coordinates: ")
    if user_input2 in bombs_placement:
        print("You win!")

else: 
    print("You loose.")
