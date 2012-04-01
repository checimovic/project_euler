#! /usr/bin/python

# Project Euler problem 42

# http://projecteuler.net/problem=42

from math import sqrt

def is_triangle(word):
    word_value = sum([ord(c) - ord('A') + 1 for c in word])

    # t(n) = 1/2(n(n+1), solve for n: n^2 + n - 2(word_value) = 0. 
    # If it's an integer, then we have a triangle word.
    n = (-1 + sqrt(1 + 8 * word_value)) / 2
    if int(n) == n: return True
    return False
     
# Read in the file.
with open("./words.txt") as f:
    words_string = f.read()
    
# Get rid of the quotes.
words = words_string.replace('"', '').split(',')

print len([word for word in words if is_triangle(word)])
