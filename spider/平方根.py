# -*- coding: utf-8 -*-
"""
Created on Mon Sep 08 21:07:10 2014

@author: shunxu
"""

x = input('Input: ')
 
low = 0
high = x

ans = (low + high) / 2.0

while ans**2 != x:
    if ans**2 < x:
        low = ans
    else:
        high = ans
        
    ans = (low + high) / 2.0
 
print ans


