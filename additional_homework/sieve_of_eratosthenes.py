"""
Write a Python program using Sieve of Eratosthenes method for computing primes up to a specified number.
Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) 
one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
"""

def sieve_of_eratosthenes(limit):
    prime_numbers = []
    multiples = []

    for i in range(2, limit + 1):
        if i not in multiples:
            prime_numbers.append(i)
            multiples.extend([x * i for x in range(limit // i + 1)])
        
    return prime_numbers


print(sieve_of_eratosthenes(100))