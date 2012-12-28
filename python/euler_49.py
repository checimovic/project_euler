#! /usr/bin/python

# Project Euler problem 49

# http://projecteuler.net/problem=49

from itertools import permutations as perms

# This is lifted from:
# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
def rwh_primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]
 
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
   
# Checks if c is a permution of p.
def is_perm(c, p):
    all_perms = [int(''.join(s)) for s in perms(str(p))]
    if c in all_perms: return True

# Checks if we have a candidate permuation of p.
def is_candidate(c, p):
    return is_prime(c) and is_perm(c, p)

all_primes = rwh_primes2(9999)
primes = [p for p in all_primes if p > 1487]

# This was tricky: it wasn't obvious from the problem that the primes 
# must be 3330 from each other.
for p in primes:
    a = p + 3330
    b = a + 3330
    if is_candidate(a, p) and is_candidate(b, p):
        print "%d%d%d" % (p, a, b)
        break
