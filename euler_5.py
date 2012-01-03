#! /usr/bin/python

# Project Euler problem 5

"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# No point in starting small. Put in all the primes and 9 and 16 which
# picks up the other factors.
num = 5 * 7 * 9 * 11 * 13 * 16 * 17 * 19
done = False

# Check our answer.
while not done:
    for divisor in xrange(1, 21):
        print "num = %d, divisor = %d" % (num, divisor)
        if num % divisor != 0:
            break
        
        if divisor == 20:
            done = True
            print num
            break
    
    