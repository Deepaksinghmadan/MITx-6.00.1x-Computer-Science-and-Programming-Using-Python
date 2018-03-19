# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:57:15 2018

@author: deepak
"""

n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()