# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 21:09:07 2018

@author: deepak
"""

n=int(input("Enter upper limit of range: "))
sieve=set(range(2,n+1))
while sieve:
    prime=min(sieve)
    print(prime,end="\t")
    sieve-=set(range(prime,n+1,prime))