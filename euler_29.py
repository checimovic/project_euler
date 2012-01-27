#! /usr/bin/python

# Project Euler problem 29

# http://projecteuler.net/problem=29

print len(set([a**b for a in range(2, 101) for b in range(2, 101)]))

