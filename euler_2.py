#! /usr/bin/python

# Project Euler problem 2

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
            print "%d, %d" % (fib_num, total)
        else:
            done = True
    
print total
