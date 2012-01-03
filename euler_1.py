#! /usr/bin/python

# Project Euler problem 1

total = 0

for n in xrange(1000):
    if (n % 3 == 0) or (n % 5 == 0):
        total += n

print total
