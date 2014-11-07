# -*- coding: utf-8 -*-
"""
Created on Mon Aug 04 00:09:32 2014

@author: shunxu
"""

def swap(lst,a,b):
    c = lst[a]
    lst[a] = lst[b]
    lst[b] = c
    
    
    
def shift_left(lst):
    tmp = lst[0]
    for i in range(len(lst)-1):
        lst[i] = lst[i+1]
    
    lst[-1] = tmp

x = [10,20,30]

shift_left(x)
#print x

def f(l):
    l[1] = [5]
    return l
     
a = [1, 2, 3]
f(a)
print a[1]