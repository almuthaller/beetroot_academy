# The valid phone number program.
#
# Make a program that checks if a string is in the right format for a phone number. 
# The program should check that the string contains only numerical characters and is only 10 characters long. 
# Print a suitable message depending on the outcome of the string evaluation.

phone_number = input("Please type your phone number.")
number_of_characters = len(phone_number) 
if number_of_characters > 10:
    print("Your phone number can only be 10 characters long.")  #I was unsure if "only 10 characters" means exactly 10 or not more than 10. I decided to go with "it can't be longer than 10"
if not phone_number.isdigit():                                  #Question: What does phone_number.isdigit do if I don't add the ()? It doesn't give me an error so I guess the code still runs.
    print("Your phone number can only contain digits.")
else: 
    print("This is a valid phone number.")
