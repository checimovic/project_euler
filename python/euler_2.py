#! /usr/bin/python

# Project Euler problem 2

"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

def fib():
    a, b = 0, 1
    
    while 1:
        yield a
        a, b = b, a + b
            
done = False
total = 0
fib_gen = fib()
    
while not done:
    fib_num = fib_gen.next()
    
    if fib_num % 2 == 0:
        if fib_num <= 4000000:
            total += fib_num
        else:
            done = True
    
print total