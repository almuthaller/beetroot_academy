"""
Write a Python program using Sieve of Eratosthenes method for computing primes up to a specified number.
Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) 
one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
"""

import math


def sieve_of_eratosthenes(limit):
    prime_numbers = set(range(2, limit + 1))
    for element in range(2, limit):
        if element in prime_numbers:
            for number in range(2, limit // element + 1):
                prime_numbers.discard(number * element)

    return list(prime_numbers)


print(sieve_of_eratosthenes(123))