#! /usr/bin/python

# Project Euler problem 44

# http://projecteuler.net/problem=44

from math import sqrt, fabs

'''Use the quadratic equation to see if a number is pentagonal.'''
def is_pentagonal(p):
    p = fabs(p)
    n = (1 + sqrt(1 + 24*p))/6
    return n == int(n)
    
def make_pentagonal(n):
    while True:
        yield (n*(3*n - 1))/2
        n += 1

pents = make_pentagonal(1)
pent_list = []
found = False

while not found:
    p1 = pents.next()
    i = len(pent_list)
    
    for x in range(i):
        p2 = pent_list[x]

        if is_pentagonal(p1 - p2) and is_pentagonal(p1 + p2):
            print "Found: %d" % (p1 - p2)
            found = True
            break
    pent_list.append(p1)
        
