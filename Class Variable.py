# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:46:51 2017

@author: deepak
"""

class animals():
    def __init__(self, age):
        self.age=age
        self.name=None
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self,newname=" "):
        self.name=newname
        
    def set_age(self,newage):
        self.age=newage
        
    def __str__(self):
        return "animal"+ ": " +str(self.name)+ ":" +str(self.age)
    
class Rabbit(animals):
    tag=1
    def __init__(self,age,parent1=None,parent2=None):
        animals.__init__(self,age)
        self.parent1=parent1
        self.parent2=parent2
        self.ridd=Rabbit.tag
        Rabbit.tag +=1
        
    def get_rid(self):
        return str(self.ridd).zfill(3)
        
    def get_parent1(self):
        return self.parent1
    
    def get_parent2(self):
        return self.parent2
    
    def __add__(self,other):
        return Rabbit(0, self, other)
    
    
    
    
        
            
    
        
    
        
    