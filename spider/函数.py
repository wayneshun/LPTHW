# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 22:37:58 2014

@author: shunxu
"""

def sum(i1, i2):
    result= 0
    for i in range(i1, i2 + 1):
        result = result + i
    return result

print sum(1, 100)