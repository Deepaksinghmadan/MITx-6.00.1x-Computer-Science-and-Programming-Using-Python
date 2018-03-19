# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:15:15 2018

@author: deepak
"""

a=int(input("Enter the number  -"))
b=[]
for i in range(1,a+1):
    print(i,sep="",end=" ")
    if(i<a):
        print('+',sep="",end=" ")
    b.append(i)
print("=",sum(b))
