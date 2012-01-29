#! /usr/bin/python

# Project Euler project 32

# http://projecteuler.net/problem=32

# Checks if two numbers contain any identical digits.
def disjoint(x, y):
    return set(str(x)).isdisjoint(set(str(y)))

# Check if a number only contains unique digits.    
def unique(x):
    return len(str(x)) == len(set(str(x)))
 
# Check if x * y = z is 1..9 pandigital.
def pandigital(x, y, z):
    if disjoint(x, y) and disjoint(x, z) and disjoint(y, z) and unique(x) and unique(y) and unique(z):
        pan = str(x) + str(y) + str(z)
        if pan.find('0') > 0: return False
        return len(pan) == 9
    
# The ranges were found by "experimentation".
print sum(set([x*y for x in range(4, 500) for y in range(12, 2000) if pandigital(x, y, x*y)]))
