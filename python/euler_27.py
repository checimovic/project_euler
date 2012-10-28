#! /usr/bin/python

# Project Euler problem 27

"""http://projecteuler.net/problem=27

The solution will take the form of n**2 - (2q-1)n + (41+q**2-q),
where q is between 0..40."""

for q in range (40, 0, -1):
    a = 2 * q - 1
    b = 41 + (q * q) - q
    
    if a < 1000 and b < 1000:
        prod = -a * b
        break
        
print prod
