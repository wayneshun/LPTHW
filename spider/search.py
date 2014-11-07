# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 23:23:14 2014

@author: shunxu
"""

def search(lst,a):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) / 2
        if lst[mid] > a:
            high = mid - 1
        elif lst[mid] < a:
            low = mid + 1
        else:
            return mid
    return -1
        

x = [1,2,3,4,5,6,7]

i = search(x,5)
print i