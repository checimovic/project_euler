#! /usr/bin/python

# Project Euler problem 43

# http://projecteuler.net/problem=43

# This problem succumbs to analysis. The end result of this is that the
# pandigitals must end with either 357289 or 952867, making the first
# four digits a matter of checking each permutation of 1460 and 1430,
# respectively.

from itertools import permutations as perms
 
def is_curious(n_str):
    if int(n_str[1:4]) % 2 != 0: return False
    if int(n_str[2:5]) % 3 != 0: return False
    return True

def create_pandigitals(start, end):
    total = 0
    for s in perms(start):
        n = ''.join(s)
        poss = n + end
        if is_curious(poss): total += int(poss)
    return total
    
print create_pandigitals('1460', '357289') + create_pandigitals('1430', '952867')


