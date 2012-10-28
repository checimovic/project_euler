#! /usr/bin/python

# Project Euler problem 38

# http://projecteuler.net/problem=38

def is_pandigital(num):
    num_set = set(num)
    if len(num_set) is 9 and '0' not in num_set: return True
    return False
    
for n in range(9876, 9123, -1):
    pan = str(n * 1) + str(n * 2)
    if is_pandigital(pan):
        print pan
        break
