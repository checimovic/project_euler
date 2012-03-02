#! /usr/bin/python

# Project Euler problem 36

"""The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""

palindromes = []

for n in range(1, 1000000):
    n_bin = bin(n)[2:]
    if n == int(str(n)[::-1]) and n_bin == n_bin[::-1]:
        palindromes.append(n)

print sum(palindromes)

        