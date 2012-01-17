#! /usr/bin/python

# Project Euler problem 22

"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?"""

# Compute the value of a name by adding up the ordinal values of its
# characters.
def name_value(name):
    return sum([ord(c) - ord('A') + 1 for c in name])

# Read in the file.
with open("./names.txt") as f:
    names_string = f.read()
    
# Get rid of the quotes and sort the names.
names = names_string.replace('"', '').split(',')
names.sort()

# Zip the names with their position in the list.
names = zip(names, range(1, len(names) + 1))

print sum([name_value(n[0]) * n[1] for n in names])
