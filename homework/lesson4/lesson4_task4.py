# The math quiz program

# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, 
# and then responds with a message accordingly.

right_answer = (357 / 7)
user_answer = int(input("What is 357 divided by 7? "))

if user_answer == right_answer:
    print("Well done, that's right!")
else:
    print("Eeeeh nope.")