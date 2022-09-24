"""
Create simple timer, for 1 minute. Once 1 minute will past - print It's time!
"""

from datetime import datetime, timedelta


current_time = datetime.now()
end_time = current_time + timedelta(minutes = 1)

while end_time > datetime.now():
    pass

print("It's time!")


# Advanced - every 10 seconds print a message. 

expected_datetime = datetime.now() + timedelta(seconds=10)

while True:
    if datetime.now() > expected_datetime:
        print("Ten seconds have passed.")
        expected_datetime = datetime.now() + timedelta(seconds=10)