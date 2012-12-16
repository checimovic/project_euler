#! /usr/bin/python

# Project Euler problem 43

# http://projecteuler.net/problem=43

from itertools import permutations as perms

def is_pandigital(n_str):
    if n_str[0] == '0': return False
    for i in n_str:
        if int(i) > len(n_str):
            return False
    return has_unique_digits(n_str, 10)
    
def is_curious(n_str):
    if int(n_str[1:4]) % 2 != 0: return False
    if int(n_str[2:5]) % 3 != 0: return False
    if int(n_str[3:6]) % 5 != 0: return False
    if int(n_str[4:7]) % 7 != 0: return False
    if int(n_str[5:8]) % 11 != 0: return False
    if int(n_str[6:9]) % 13 != 0: return False
    if int(n_str[7:10]) % 17 != 0: return False
    return True
 
def has_unique_digits(n, num_digits):
    n_len = len(n)
    n_set = set(n)
    if n_len == num_digits and n_len == len(n_set): return True
    return False
 
primes = []

# Generate 10 digit pandigitals.
"""nums = perms(xrange(0, 10))
for s in nums:
    n = ''.join([str(i) for i in s])
    print "Trying %s" % n
    if is_pandigital(n) and is_curious(n): 
        primes.append(n)
        print "Appending %s" % n

print sum(primes)
"""