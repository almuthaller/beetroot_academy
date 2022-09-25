"""
This is a program to play rock, paper, scissors against a computer.
First one to reach a score of 5 wins the game.
"""

import random


hand = ["rock", "paper", "scissors"]
my_wins = 0
computer_wins = 0

while my_wins < 5 and computer_wins < 5:
    my_hand = input("Your choice: ")
    computers_hand = random.choice(hand)
    
    if my_hand not in hand:
        print("That is not a valid choice. Choose from 'rock', 'paper' or 'scissors'.")
        continue

    elif my_hand == computers_hand:
        print("That's a tie. Choose one more time.")
        continue

    elif hand[hand.index(my_hand) - 1] == computers_hand:
        print(f"You win! The computer chose {computers_hand}.")
        my_wins += 1

    else:
        print(f"You lose. The computer chose {computers_hand}.")
        computer_wins += 1


if my_wins > computer_wins:
    print(f"Yayy! You won with a score of 5:{computer_wins}.")

else:
    print(f"Naww :( The computer won with a score of 5:{my_wins}.")