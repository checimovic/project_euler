#! /usr/bin/python

# Project Euler problem 28

"""http://projecteuler.net/problem=28"""

import math

# The top of the ne diagonal of an nxn square is n**2.
ne_list = [n*n for n in range(3, 1002, 2)]

# The nw diagonal is calculated from the ne:
# ne - n + 1. n is the current dimension of the nxn square and it
# is equal to sqrt(ne).
nw_list = [(ne - math.sqrt(ne) + 1) for ne in ne_list]

# The sw diagonal is calculated as:
# ne - 2n + 2
sw_list = [(ne - (2 * math.sqrt(ne)) + 2) for ne in ne_list]

# The se diagonal is calculated as:
# ne - 3n + 3
se_list = [(ne - (3 * math.sqrt(ne)) + 3) for ne in ne_list]

print int(sum(nw_list) + sum(ne_list) + sum(sw_list) + sum(se_list) + 1)
