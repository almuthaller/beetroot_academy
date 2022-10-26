# Password Generator
# #     1.    Password length should be from 4 to 16 symbols
# #     2.    The following options should be available for the user:
# # -  latin alphabet, upper case letters, lower case letters, punctuation symbols
# the response can be Y/N (possible usage y/n and Y/N)
#        3. Based on the given bass the password is generated randomly and given to the user

from random import choices
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def password_generator():
    length = 0
    while length < 4 or length > 16:
        length = input("How long do you want the password to be? (4 - 16 characters): ")
        if length.isdigit():
            length = int(length)
        else:
            length = 0

    password_alphabet = ""

    def ask_user(question, alphabet_extension):
        nonlocal password_alphabet
        while True:
            user_answer = input(f"Do you want to use {question} (y/n): ")
            if user_answer == "y":
                password_alphabet += alphabet_extension
                break
            elif user_answer == "n":
                break
            else:
                print("Please type y or n.")

    ask_user("lowercase letters", ascii_lowercase)
    ask_user("uppercase letters", ascii_uppercase)
    ask_user("digits", digits)
    ask_user("symbols", punctuation)

    password = "".join(choices(password_alphabet, k=length))
    print(password)


password_generator()
