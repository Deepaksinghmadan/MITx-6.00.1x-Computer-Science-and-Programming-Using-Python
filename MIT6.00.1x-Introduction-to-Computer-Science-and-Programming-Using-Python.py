# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 00:22:29 2017

@author: deepak
"""
s='abcdef'
i=1
subs1=s[0]
subs2=s[0]
while(i<len(s)):
    j=i
    while(j<len(s)):
        if(s[j]>=s[j-1]):
            subs1+=s[j]
            j+=1 
        else:
            subs1=subs1.replace(subs1[:len(subs1)],s[i])   
            break
                
        if(len(subs1)>len(subs2)):
            subs2=subs2.replace(subs2[:len(subs2)], subs1[:len(subs1)])
    subs1=subs1.replace(subs1[:len(subs1)],s[i])
        
    if(len(subs1)==len(s)):
        subs2=subs2.replace(subs2[:len(subs2)], subs1[:len(subs1)])
        print( "not here" )   
        break;     
            
    i+=1
print ("Longest substring in alphabetical order is:",subs2)
               