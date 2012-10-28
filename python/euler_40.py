#! /usr/bin/python

# Project Euler problem 40  

# http://projecteuler.net/problem=40

n = ''.join([str(n) for n in range(1000001)])
print int(n[10]) * int(n[100]) * int(n[1000]) * int(n[10000]) * int(n[100000]) * int(n[1000000])
