#! /usr/bin/python

# Project Euler problem 7

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?"""

import math

def isprime(n):
    # 0 and 1 are not primes.
    if n < 2:
        return False
        
    # 2 is the only even prime number.
    if n == 2: 
        return True
        
    # All other even numbers are not primes.
    if not n & 1: 
        return False
        
    # Primes > 3 must take the form of 6k +/- 1.
    if n > 3:
        test_high = n + 1
        test_low = n - 1
    
        if test_high % 6 != 0 and test_low % 6 != 0:
            return False
        
    # Start with 3 and only go up to the square root of n
    # for all odd numbers.
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
            
    return True

n = 10001
prime_list = [2]
possible_prime = 3

while len(prime_list) < 10001:
    if isprime(possible_prime):
        prime_list.append(possible_prime)
    
    possible_prime += 2

print(prime_list[10000])

