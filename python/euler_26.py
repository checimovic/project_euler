#! /usr/bin/python

# Project Euler problem 26

"""http://projecteuler.net/problem=26"""

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

length = 0
denom = 0
base = 10

# This algorithm comes from Wikipedia. Since all cyclic numbers are
# the result of 1/p where p is prime, this computes the digits of 1/p by 
# long division and tests to see if the result is cyclic.
for p in range(0, 1001):
    if not isprime(p) or base % p == 0: continue
    
    t = 0
    r = 1
    n = 0
    
    while(True):
        t += 1
        x = r * base
        d = x/p
        r = x % p
        n = n * base + d
        
        if r != 1: continue
        
        if t == p - 1:
            l = len(str(n))
            if l > length:
                length = l
                denom = p
                
        break
                
print denom    
    
    
    
"""test = (10**(p-1) - 1)/p
    
    if (test * p) % 9 == 0:
        l = len(str(test))
        
        if l > length: 
            length = l
            d = p

print d
"""