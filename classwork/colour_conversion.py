"""
Type conversion. Several different formats are used to represent color. 

For example, the primary format for LCD displays, digital cameras, and web pages—known as 
the RGB format—specifies the level of red (R), green (G), and blue (B) on an integer scale from 0 to 255. 
The primary format for publishing books and magazines—known as the CMYK format—specifies the level of 
cyan (C), magenta (M), yellow (Y), and black (K) on a real scale from 0.0 to 1.0.

Create a program that after the start, indefinitely waits for user input in CMYK format 
and on each input converts to RGB and prints response in the format (equal sign should be on the same level):
red    = 255
green  = 0
blue   = 255 

Formula:
white  = 1 - black
red    = 255 x white x (1 - cyan)
green  = 255 x white x (1 - magenta)
blue   = 255 x white x (1 - yellow)

As the input program waits for parameters like 0.0 1.0 0.0 0.0 (4 numbers split by space character). 
Pay attention that we can use python strings split method to get all params, but it will require 
covering lighting explanation on python lists, thus I suggest to write custom logic using while and if statements 
to validate obtained results.

The program should terminate after receiving as input exit or e string. 
Also, the program needs to have logic to check for the right input format and in case of passing wrong parameters 
should print a suitable message via print and continue waiting for input.
"""

user_input = input("Enter your values or enter exit")

while user_input != "exit":
    [cyan, magenta, yellow, black] = user_input.split(" ")
    white = 1 - float(black)
    red = 255 * white * (1-float(cyan))
    green = 255 * white * (1-float(magenta))
    blue = 255 * white * (1-float(yellow))                                      
    print(f"Red: {red}")
    print(f"Green: {green}")
    print(f"Blue: {blue}")
    user_input = input("Enter your values or enter exit")    