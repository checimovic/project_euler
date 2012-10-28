#! /usr/bin/python

# Project Euler problem 24

"""What is the first term in the Fibonacci sequence to contain 1000 digits?"""

def fib():
    a, b = 0, 1
    
    while 1:
        yield a
        a, b = b, a + b
   
for i, f in enumerate(fib()):
    if len(str(f)) == 1000: break
    
print i
