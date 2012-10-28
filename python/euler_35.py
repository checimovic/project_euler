#! /usr/bin/python

# Project Euler problem 35

# http://projecteuler.net/problem=35

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

def cycle_number(num, times):
    num_string = str(num)
    for i in range(0, times):
        num_string = num_string[1:] + num_string[0]
    return int(num_string)
    
circular_primes = set()

for n in range(3, 1000000, 2):
    circ_prime = True
    
    if isprime(n):
        for i in range(1, len(str(n))):
            n_cycled = cycle_number(n, i)
            
            if not isprime(n_cycled):
                circ_prime = False
                break
                        
        if circ_prime: circular_primes.add(n)
   
# Add one because 2 is prime and we aren't testing for it above.
print len(circular_primes) + 1

