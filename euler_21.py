#! /usr/bin/python

# Project Euler problem 21

"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10,000."""

import math

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

def amicable(a):
    b = sum(get_divs(a))
    
    if a == b: return 0
    
    sum_b_divs = sum(get_divs(b))
    
    if a == sum_b_divs:
        return b
        
    return 0

print sum([amicable(i) for i in range(1, 10000)])
    