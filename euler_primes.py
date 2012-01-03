#! /usr/bin/python

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
            
