"""
Create a class method named validate, 
which should be called from the __init__ method to validate parameter email, passed to the constructor. 
The logic inside the validate method could be to check if the passed email parameter is a valid email string.

Email validations:

    Valid email address format: https://help.xmatters.com/ondemand/trial/valid_email_format.htm
    Wiki: Email address: https://en.wikipedia.org/wiki/Email_address
"""

import re


class Contact:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        self.valid_format = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.match(self.valid_format, self.email):
            raise ValueError("This is not a valid email address.")


my_contact = Contact("almut.haller@gmail.com")

was_error_raised = False
try:
    invalid_contact = Contact("almut.haller.gmail.com")
except ValueError:
    was_error_raised = True

assert was_error_raised

another_invalid_contact = Contact("almut.com")