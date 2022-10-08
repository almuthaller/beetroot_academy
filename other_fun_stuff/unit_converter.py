"""
This is a program to quickly convert American to European units and vice versa.
"""


def convert(value, unit):
    # for temperatures
    if unit == "°C":
        output_value, output_unit = value * 9 / 5 + 32, "°F"
    elif unit == "°F":
        output_value, output_unit = (value - 32) * 5 / 9, "°C"

    # for length measurements
    elif unit == "cm":
        output_value, output_unit = value / 2.54, "”"
    elif unit == "”":
        output_value, output_unit = value * 2.54, "cm"

    # for undefined unit
    else:
        raise ValueError("There is currently no function to convert from this unit.")

    return f"= {round(output_value, 2)}{output_unit}"


assert convert(13, "°C") == "= 55.4°F"
assert convert(23, "°F") == "= -5.0°C"

assert convert(40, "cm") == "= 15.75”"
assert convert(5, "”") == "= 12.7cm"


while True:
    user_input = input()
    if user_input == "stop":
        break

    user_value = float("".join([c for c in user_input if c.isdigit() or c == "."]))
    user_unit = "".join([c for c in user_input if not c.isdigit() and c != " "])

    print(convert(user_value, user_unit), "\n")
