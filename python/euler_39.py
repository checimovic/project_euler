#! /usr/bin/python

# Project Euler problem 39

# http://projecteuler.net/problem=39

# Generate Pythagorean triplets. See problem 9.
done = False
freqs = {}

for m in range(1, 101):
    # Start by generating primitives.
    for n in range(1, m):
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        
        if a**2 + b**2 != c**2:
            continue
        
        if a + b + c > 1000: break
        
        # Generate all the triples, including non-primitives.
        for k in range(1, 100):
            sum = k*a + k*b + k*c
            
            if (sum > 1000): break
    
            test = freqs.get(sum)
            if test == None: 
                freqs[sum] = set()
            freqs[sum].add((k*a, k*b, k*c))
            
print "Most frequent: %d" % max(freqs, key=lambda a: len(freqs.get(a)))
