#! /usr/bin/python

# Project Euler problem 30

# http://projecteuler.net/problem=30

vals = []
upper_limit = 9**5 * 6

for n in range(2, upper_limit):
    t = 0
    for i in str(n):
        t += int(i)**5
        
    if t == n: vals.append(n)
      
print vals
print sum(vals)

    