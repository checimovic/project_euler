#! /usr/bin/python

# Project Euler problem 34

# http://projecteuler.net/problem=34

""" The upper limit of the search for factorions is found as follows:
any number of at least n digits is at least 10**n-1. The sum of the factorials
of an n-digit number can be no great than n*9!. So we need to find n where
10**n-1 > n*9!. """

from math import factorial as fac

# Find the upper bound of the number of digits.
n = 1
while n*fac(9) > 10**n:
    n += 1

print sum([i for i in range(3, n*fac(9)) if sum([fac(int(d)) for d in str(i)]) == i])
