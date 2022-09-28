"""
User could input to you something. You'll to transform it to int and divide 1 by this number. 
Don't use if/else blocks and print "Wrong input" in case if some exception happen
"""

try:
    user_input = input("Input something: ")
    print(1 / int(user_input))

except (ValueError, ZeroDivisionError):
    print("Wrong input")