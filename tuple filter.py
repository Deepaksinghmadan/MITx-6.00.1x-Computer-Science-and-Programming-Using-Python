# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 00:09:28 2017

@author: deepak
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    out=[]
    for i in range(len(aTup)):
       if i%2 == 0:
         out.append(aTup[i])
    return(tuple(out))