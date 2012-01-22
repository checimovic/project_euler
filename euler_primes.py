#! /usr/bin/python -i

import math
import numpy

def primer(upto):
    primes = numpy.arange(3, upto + 1, 2)
    isprime = numpy.ones((upto - 1) / 2, dtype=bool)
    
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[(factor - 2) / 2]: 
            isprime[(factor * 3 - 2) / 2::factor] = 0
            
    return numpy.insert(primes[isprime], 0, 2)
    
def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)
            
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
    