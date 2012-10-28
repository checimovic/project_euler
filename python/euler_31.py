#! /usr/bin/python

# Project Euler problem 31

# http://projecteuler.net/problem=31

combos = 0 

# The strategy is to simply iterate over each coin denomination, subtracting the running
# total from the full amount of 200p. This finds all the combinations of coins that add
# up to 200p.
for a in range(0, 200/200 + 1):
    at = 200-200*a
    for b in range(0, at/100 + 1):
        bt = at-100*b
        for c in range(0, bt/50 + 1):
            ct = bt-50*c
            for d in range(0, ct/20 + 1):
                dt = ct-20*d
                for e in range(0, dt/10 + 1):
                    et = dt-10*e
                    for f in range(0, et/5 + 1):
                        ft = et-5*f
                        for g in range(0, ft/2 + 1):
                            gt = ft-2*g
                            for h in range(0, gt + 1):
                                ht = gt-h
                                if ht == 0:
                                    combos += 1
                                    print("%s*200, %s*100, %s*50, %s*20, %s*10, %s*5, %s*2, %s*1") % (a, b, c, d, e, f, g, h)
                            
print combos
