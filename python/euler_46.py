#! /usr/bin/python

# Project Euler problem 46

# http://projecteuler.net/problem=46

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
    
def twice_square(n):
    while True:
        yield 2*(n*n)
        n += 1
    
primes = rwh_primes2(1000000)
found = False
n = 33

while not found:
    goldbach = False
    
    n += 1
    while n in primes or n % 2 == 0:
        n += 1
    
    for p in primes:
        if goldbach: break

        if p > n:
            print n
            found = True
            break
            
        for t in twice_square(1):
            if p + t == n:
                goldbach = True
                break
            if p + t > n:
                break
         
