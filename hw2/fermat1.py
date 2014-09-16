# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 20:17:22 2014

@author: gianfranco
"""

a= int(raw_input("ingrese el valor de a??:"))
b= int(raw_input("ingrese el valor de b??:"))
c= int(raw_input("ingrese el valor de c??:"))
n= int(raw_input("ingrese el valor de n??:"))
    
def check_fermat():  
    if n > 2 and (a^n)+(b^n)==c^n:
        print("Holy smokes, fermat was wrong!!")
    else:
        print("No, that does not work")
check_fermat()