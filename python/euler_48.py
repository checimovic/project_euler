#! /usr/bin/python

# Project Euler problem 48

# http://projecteuler.net/problem=48

# This one is quite trivial with Python's long integer support.

sum = 0

for n in range(1, 1001):
    sum += n**n
    
print str(sum)[-10:]

