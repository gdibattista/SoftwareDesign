# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 20:36:02 2014

@author: gianfranco
"""

x= int(raw_input("ingrese el valor de x??:"))
y= int(raw_input("ingrese el valor de y??:"))

    
def compare(x,y):  
    if x > y:
        return("1")
    if x==y:
        return("0") 
    if x < y:
        return("-1")
print compare(x,y)