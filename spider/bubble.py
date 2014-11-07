# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 23:32:15 2014

@author: shunxu
"""
def swap(lst,a,b):
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp
    
    
    
def bubble(lst):
    top = len(lst) - 1
    exchange = True
    
    while exchange:
        exchange = False
        for i in range(top):
            if lst[i] > lst[i + 1]:
                swap(lst,i,i + 1)
                exchange = True

        top = top - 1

x = [1,9,3,14,25,6,87]

i = bubble(x)

print x