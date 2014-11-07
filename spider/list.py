# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 23:03:43 2014

@author: shunxu
"""

lst = [1,2,3,4,5,6,1]

a = input("//")

t = 1

for i in range(len(lst)):
    if lst[i] == a:
        print i
        t = 0
        break

if t == 1:
    print -1
    