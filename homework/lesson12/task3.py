"""
Fraction

Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) 
with appropriate checking and error handling

class Fraction:
	pass

x = Fraction(1/2)
y = Fraction(1/4)

x + y == Fraction(3/4)
"""

import math


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("The denominator cannot be 0.")

        self.num = numerator
        self.denom = denominator

    def __repr__(self):
        return f"{self.num}/{self.denom}"

    def __eq__(self, other):
        return self.num == other.num and self.denom == other.denom

    def __ne__(self, other):
        return not (self == other)

    def cancel_fraction(self, f):
        greatest_common_divisor = math.gcd(f.num, f.denom)
        return Fraction(
            int(f.num / greatest_common_divisor), int(f.denom / greatest_common_divisor)
        )

    def __add__(self, other):
        new_fraction = Fraction(
            self.num * other.denom + other.num * self.denom, self.denom * other.denom
        )
        return self.cancel_fraction(new_fraction)

    def __sub__(self, other):
        new_fraction = Fraction(
            self.num * other.denom - other.num * self.denom, self.denom * other.denom
        )
        return self.cancel_fraction(new_fraction)

    def __mul__(self, other):
        new_fraction = Fraction(self.num * other.num, self.denom * other.denom)
        return self.cancel_fraction(new_fraction)

    def __truediv__(self, other):
        new_fraction = Fraction(self.num * other.denom, self.denom * other.num)
        return self.cancel_fraction(new_fraction)


x = Fraction(1, 2)
y = Fraction(1, 4)

assert x + y == Fraction(3, 4)
assert x - y == Fraction(1, 4)
assert x * y == Fraction(1, 8)
assert x / y == Fraction(2, 1)

assert Fraction(1, 2) == Fraction(1, 2)
assert Fraction(1, 2) != Fraction(1, 3)
assert Fraction(1, 2) != Fraction(2, 4)
