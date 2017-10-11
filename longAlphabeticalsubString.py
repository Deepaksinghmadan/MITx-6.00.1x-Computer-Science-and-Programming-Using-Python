# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:54:50 2017

@author: deepak
"""

s = 'cyqfjhcclkbxpbojgkar'
from itertools import count

def long_alphabet(input_string):
    maxsubstr = input_string[0:0] # empty slice (to accept subclasses of str)
    for start in range(len(input_string)): # O(n)
        for end in count(start + len(maxsubstr) + 1): # O(m)
            substr = input_string[start:end] # O(m)
            if len(set(substr)) != (end - start): # found duplicates or EOS
                break
            if (ord(max(sorted(substr))) - ord(min(sorted(substr))) + 1) == len(substr):
                maxsubstr = substr
    return maxsubstr

bla = (long_alphabet(s))
print "Longest substring in alphabetical order is: %s" %bla