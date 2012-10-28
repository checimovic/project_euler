#! /usr/bin/python

# Project Euler problem 9

"""A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

""" The following generates all Pythagorean triplets, given some m > n:

a = m**2 - n**2, b = 2mn, c = m**2 + n**2"""

goal = 1000
m = 2
done = False

while not done:
    for n in range(1, m - 1):
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        
        if a**2 + b**2 != c**2:
            continue
        
        # Check if the sum is a factor of the goal. If so, we can scale it up,
        # shortening the search somewhat.
        sum = a + b + c
        
        if goal % sum == 0:
            fac = goal / sum
            a *= fac
            b *= fac
            c *= fac
            sum = a + b + c
        
        if sum == goal:
            print "%d * %d * %d = %d" % (a, b, c, a * b * c)
            done = True
            break
    
    m += 1

