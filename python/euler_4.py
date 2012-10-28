#! /usr/bin/python

# Project Euler problem 4

"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

done = False
highest = 0

# Start with the big numbers, so iterate in reverse.
for x in xrange(999, 99, -1):    
    for y in xrange(999, 99, -1):
        current = x * y
        test = str(current)
        
        if test == test[::-1] and current > highest:
            highest = current
            
print highest

