#! /usr/bin/python

# Project Euler problem 17

"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""

num_lengths = \
    {1:3,
    2:3,
    3:5,
    4:4,
    5:4,
    6:3,
    7:5,
    8:5,
    9:4,
    10:3,
    11:6,
    12:6,
    13:8,
    14:8,
    15:7,
    16:7,
    17:9,
    18:8,
    19:8,
    20:6,
    30:6,
    40:5,
    50:5,
    60:5,
    70:7,
    80:6,
    90:6}
    
total = 0
    
def get_num_length(n):
    length = 0
    
    # Check if it's already in there.    
    try:
        return num_lengths[n]
    except KeyError:
        pass
    
    # Special case.
    if n % 1000 == 0:
        return 11
        
    # Get the hundreds.
    if n // 100 > 0:
        length += num_lengths[n // 100] + len("hundred")
        n = n % 100
        
        # If there's a remainder, add the length of "and".
        if n > 0: length += len("and")
        
    # Get the tens.
    if n // 10 > 0:
        try:
            length += num_lengths[n]
            return length
        except KeyError:
            pass
            
        length += num_lengths[(n // 10) * 10]
        n = n % 10
        
    # Get the ones.
    if n > 0:
        length += num_lengths[n]
        
    return length
    
print sum(map(get_num_length, range(1, 1001)))

