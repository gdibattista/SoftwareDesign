# -*- coding: utf-8 -*-
"""
Random_art.py

@author: amonmillner, adapted from pruvolo work
"""

# you do not have to use these particular modules, but they may help
from random import randrange
import Image
from math import *

def prod(a,b):
    return float(a)*float(b)

def cos_pi(a):
    return cos(pi*a)
    
def sin_pi(a):
    return sin(pi*a)

def x(a):
    return float(a)

def y(b):
    return float(b)
    
def xmenos(a):
    return float(-a)
    
def ymenos(b):
    return float(-b)


def crea_funcion(depth):
    if depth == 1:
        variable=[['x'],['y']]
        return variable[randrange(len(variable))]     
    
    funciones=['prod','cos_pi','sin_pi','xmenos','ymenos']
    funcion1=funciones[randrange(len(funciones))]
    
    if funcion1  == 'prod':
        return [funcion1, crea_funcion(depth -1), crea_funcion(depth -1)]
    else:
        return [funcion1, crea_funcion(depth -1)]

def build_random_function(min_depth, max_depth):
    depth = randint(min_depth,max_depth)
    return crea_funcion(depth)
    
func = build_random_function(1,5)        
print func  
        
        
        
def evaluate_random_function(f, x, y):
    if f[0]=='x':
        return x
    elif f[0]=='prod':
        return prod(evaluate_random_function(f[1],x,y), evaluate_random_function(f[2],x,y))
    elif f[0]=='cos_pi':
        return cos_pi(evaluate_random_function(f[1],x,y)) 
    elif f[0]=='sin_pi':
        return sin_pi(evaluate_random_function(f[1],x,y)) 
    elif f[0]=='xmenos':
        return float(-x)
    if f[0]=='ymenos':
        return float(-y)
    elif f[0]== 'y':
        return y
print evaluate_random_function(func,1,3)


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
        
   
    convert = float(output_interval_end -output_interval_start )*float(val - input_interval_start)/(input_interval_end -input_interval_start)
    output1 =output_interval_start + convert* (output_interval_end - output_interval_start)
    return output1

for i in range(5):

    foto = Image.new("RGB", (350,350))
    green = build_random_function(5,10)
    blue = build_random_function(5,10)
    red = build_random_function(5,10)
    for x in range(0,349):
        for y in range(0,349):
            blue1= remap_interval(evaluate_random_function(blue, remap_interval(x,0,349,-1,1), remap_interval(y,0,349,-1,1)),-1,1,0,255)
            green1= remap_interval(evaluate_random_function(green, remap_interval(x,0,349,-1,1), remap_interval(y,0,349,-1,1)),-1,1,0,255)
            red1= remap_interval(evaluate_random_function(red, remap_interval(x,0,349,-1,1), remap_interval(y,0,349,-1,1)),-1,1,0,255)
            foto.putpixel((x,y),(int(red1),int(green1),int(blue1)))
    foto.save("ejemplo"+str(i+1)+".png","PNG")

#your additional code and functions go here
