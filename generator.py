# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 17:12:27 2017

@author: deepak
"""

def genprimes(upto):
    primes = {}
    q = 2
    i = 0
    while i < upto:
        if q not in primes:
            yield q
            i += 1
            primes[q*q] = [q]
        else:
            for p in primes[q]:
                primes.setdefault(p+q, []).append(p)
            del primes[q]
        q += 1
        
f = genprimes(20)
