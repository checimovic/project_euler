#! /usr/bin/python

# Project Euler problem 18

# For a complete description: http://projecteuler.net/problem=18

T = "\
75;\
95 64;\
17 47 82;\
18 35 87 10;\
20 04 82 47 65;\
19 01 23 75 03 34;\
88 02 77 73 07 63 67;\
99 65 04 28 06 16 70 92;\
41 41 26 56 83 40 80 70 33;\
41 48 72 33 47 32 37 16 94 29;\
53 71 44 65 25 43 91 52 97 51 14;\
70 11 33 28 77 73 17 78 39 68 17 57;\
91 71 52 38 17 14 91 43 58 50 27 29 48;\
63 66 04 68 89 53 67 30 73 16 69 87 40 31;\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

# Clean the data - remove leading zeros on numbers and put the whole thing
# into a list of lists of ints.
nums_list = [[n for n in nums.split(' ')] for nums in T.split(';')]
triangle = [[int(j[1:]) if j[0] == '0' else int(j) for j in i] for i in nums_list]

previous = -1
total = 0
rownum = 0

for row in triangle:
    option1 = row[min(previous + 1, rownum)]
    option2 = row[previous]
    print "%d, %d" % (option1, option2)
    
    if option1 > option2:
        previous += 1
        total += option1
        print option1
    else:
        total += option2
        print option2
    
    rownum += 1

print total

    
    
        