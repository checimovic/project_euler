#! /usr/bin/python

# Project Euler problem 3

"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

def prime_factors(n):
    factors = []
    lastresult = n
     
    # 1 is a special case.
    if n == 1:
        return [1]
     
    while lastresult != 1:
        c = 2
         
        while lastresult % c != 0:     
            c += 1
         
        factors.append(c)
        lastresult /= c
        
    return factors

num = 600851475143

print prime_factors(num)[-1]
