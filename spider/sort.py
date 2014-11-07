# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 22:43:43 2014

@author: shunxu
"""

def swap(lst,a,b):
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp


def select_sort(lst):
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i,len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        swap(lst,i,min_index)
        

x = [12,14,78,1,2,35]

select_sort(x)

print x
