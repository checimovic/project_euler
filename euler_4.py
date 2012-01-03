#! /usr/bin/python

# Project Euler problem 4

done = False

# Start with the big numbers, so iterate in reverse.
for x in xrange(999, 99, -1):
    if done == True: break
    
    for y in xrange(999, 99, -1):
        test = str(x * y)
        
        if test == test[::-1]:
            print "%d * %d = %s" % (x, y, test)
            done = True
            break
            

