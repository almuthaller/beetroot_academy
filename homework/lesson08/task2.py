# Write a function that takes in two numbers from the user via input(), call the numbers a and b, 
# and then returns the value of squared a divided by b, construct a try-except block which raises an exception 
# if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).    

def todays_function():
    (a, b) = input("Input two numbers: ").split(", ")
    try:
        return int(a) ** 2 / int(b)       
    except ValueError: 
        raise Exception("Input must be numbers.")
    except ZeroDivisionError:
        raise Exception("Cannot divide by 0.")


try:
    result = todays_function()
    print(result)
except Exception as ex:
    print("Error.", str(ex))