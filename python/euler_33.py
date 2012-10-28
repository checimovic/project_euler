#! /usr/bin/python

# Project Euler problem 33

# http://projecteuler.net/problem=33

from fractions import Fraction

def common_num(x, y):
    common = set(str(x)).intersection(set(str(y)))
    if len(common) > 0: return int(common.pop())
    else: return 0
    
def has_zero(x):
    return x % 10 == 0
    
def double_digit(x):
    return x % 11 == 0
    
def remove_common(x, common):
    return int(str(x).replace(str(common), ''))

prod = 1
    
for x in range(10, 100):
    if has_zero(x) or double_digit(x): continue
    for y in range(10, 100):
        if x >= y or has_zero(y) or double_digit(y): continue
        common = common_num(x, y)
        if common > 0:
            orig_fraction = Fraction(x, y)
            new_fraction = Fraction(remove_common(x, common), remove_common(y, common))
            if orig_fraction == new_fraction:
                prod *= new_fraction

print Fraction(prod).denominator
