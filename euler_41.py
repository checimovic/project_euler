#! /usr/bin/python

# Project Euler problem 41

# http://projecteuler.net/problem=41

from itertools import permutations as perms

def is_prime(n):
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

def is_pandigital(n_str):
    if '0' in n_str: return False
    for i in n_str:
        if int(i) > len(n_str):
            return False
    n_len = len(n_str)
    n_set = set(n_str)
    if n_len == len(n_set): return True
    return False
    
primes = []

# Generate all pandigital permutations, starting with 7 digit numbers and working down.
for x in range(8, 5, -1):
    nums = perms(xrange(1, x))
    for s in nums:
        n = ''.join([str(i) for i in s])
        if is_pandigital(n) and is_prime(int(n)):
            primes.append(int(n))
            
primes.sort()
print primes[len(primes) - 1]
        
