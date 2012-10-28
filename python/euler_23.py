#! /usr/bin/python

# Project Euler problem 23

"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

import math
import itertools

# This is inefficient.
def get_divs(n): 
    divs = [1]  
    check = 2  
    rootn = math.sqrt(n)
    
    while check < rootn:  
        if n % check == 0:  
            divs.append(check)  
            divs.append(n / check)  
        check += 1
        
    if rootn == check:  
        divs.append(check)  
        divs.sort()
    
    return divs 

# Cache our possibly-abundant integers here. The key is the number, the value is boolean.    
abundant_dict = {}

# Return whether or not a number is abundant. Cache the answer.
def abundant(n):
    try:
        return abundant_dict[n]
    except KeyError:
        pass
    
    abundant_dict[n] = sum(get_divs(n)) > n
    
    return abundant_dict[n] 
    
# Return whether or not a number is the sum of two abundant numbers.
def is_abundant_sum(n):
    for i in range(1, n//2 + 1):
        
        if abundant(i) and abundant(n-i):
            return True
    
    return False
    
print sum([n for n in range(1, 28123) if not is_abundant_sum(n)])

