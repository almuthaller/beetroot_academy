"""
Custom exception

Create your custom exception named CustomException, you can inherit from base Exception class, 
but extend its functionality to log every error message to a file named logs.txt. 
Tips: Use __init__ method to extend functionality for saving messages to file

class CustomException(Exception):
	def __init__(self, msg):
		...
"""

class CustomException(Exception):
	def __init__(self, msg):
		super().__init__(msg)
		self.file = open("logs.txt", "a")
		self.file.write(msg)
		self.file.close()


try:
	raise CustomException("error message hi")
except CustomException as ce:
	print(ce)