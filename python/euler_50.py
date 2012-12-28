#! /usr/bin/python

# Project Euler problem 50

# http://projecteuler.net/problem=50

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
    
primes = rwh_primes2(1000000)

total = 0
num_primes = 0
primes_len = len(primes)

for i in range(primes_len):
    # Start j at i+20 because we know the greatest number of consecutive primes below
    # 1000 is 21, according to the problem definition.
    for j in range(i + 20, primes_len):
        current = sum(primes[i:j+1])
        
        # Again according to the problem definition.
        if current <= 953: continue
        
        if current < 1000000 and is_prime(current) and j-i > num_primes:
            num_primes = j-i
            total = current
            
        if current > 1000000: break
    
print total
