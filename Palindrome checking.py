# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:50:57 2018

@author: deepak
"""

#check weather palindrome
a=int(input("Enter the number   "))
t=a
rev=0
while(a>0):
    d=a%10
    rev=rev*10+d
    a=a//10
if(t==rev):
    print("Number is palindrome")
else:
    print("Enter number is not palindrome")
    
    