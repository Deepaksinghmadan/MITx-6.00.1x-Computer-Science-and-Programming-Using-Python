# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 23:46:39 2017

@author: deepak
"""

def genprimes():
    yield 2
    prime=[2]
    a=3
    while True:
        for i in prime:
            if a % i==0:
                break
            else:
                prime.append(a)
                yield a
            a += 2
          
          
a = genprimes()




