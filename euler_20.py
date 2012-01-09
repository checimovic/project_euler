#! /usr/bin/python

# Project Euler problem 20

"""n! means n x (n x 1)  ... x 3 x 2 x 1

For example, 10! = 10 x 9  ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""

def fact(n):
    factorial = 1
    
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

print sum([int(i) for i in str(fact(100))])
