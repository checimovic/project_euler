#! /usr/bin/python

# Project Euler problem 45

# http://projecteuler.net/problem=45

from math import sqrt, fabs

'''Use the quadratic equation to see if a number is pentagonal.'''
def is_pentagonal(p):
    p = fabs(p)
    n = (1 + sqrt(1 + 24*p))/6
    return n == int(n)
    
'''Use the quadratic equation to see if a number is hexagonal.'''
def is_hexagonal(h):
    h = fabs(h)
    n = (1 + sqrt(1 + 8*h))/4
    return n == int(n)
    
def make_triangular(n):
    while True:
        yield (n * (n + 1))/2
        n += 1
    
for t in make_triangular(286):
    if is_pentagonal(t) and is_hexagonal(t):
        print t
        break
