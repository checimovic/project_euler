#! /usr/bin/python

# Project Euler problem 15

"""Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?"""

"""This is an application of the binomial theorem. If n is the number of
squares to a side, then there are 2n steps required to get to the lower
right corner - n steps down D, and n steps right R:

RRDD
RDRD
DRDR
DDRR
RDDR
DRRD

We want to find the number of ways to take n steps down (or right) out of 
the total number of steps - in other words, 2n take n.

The formula for n take k is n!/k!(n-k)!

If 2n = total number of steps, and n = number of steps in any one direction:

2n!/n!(2n - n)!"""

from math import factorial as fact

num_steps = 40
one_dir = 20

print fact(num_steps) / (fact(one_dir) * fact(num_steps - one_dir))
