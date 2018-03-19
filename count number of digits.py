# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:36:49 2018

@author: deepak
"""

# count number of digits
a=int(input("Enter the number  "))
n=0
while(a > 0):
    n = n+1
    a = a//10
print(n)


