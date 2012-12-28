#! /usr/bin/python

# Project Euler problem 47

# http://projecteuler.net/problem=47

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
    
# Trial division factorisation, taken from Wikipedia.
def factor(n):
    if n == 1: return [1]
    primes = rwh_primes2(int(n**0.5) + 1)
    prime_factors = []
 
    for p in primes:
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1: prime_factors.append(n)
 
    return prime_factors

# Smallest number to have four prime factors.    
n = 2*3*5*7
count = 0

while count < 4:
    n += 1
    factors = set(factor(n))
    
    if len(factors) == 4:
        count += 1
    else:
        count = 0

# Print the first number in the four number series.
print n-3
