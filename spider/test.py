# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 23:03:13 2014

@author: shunxu
"""

def is_up(string):
    p = string[0]
    c = string[1]
    for c in string:
        if p > c:
            return False
        else:
            p = c
    return True


f = open('names.txt')

for line in f:
    name = line.strip()
    if is_up(name):
        print name

def is_name(string):
    low = 0
    up = len(string) - 1
    while low < up:
        if string[low] != string[up]:
            return False
        else:
            low = low + 1
            up = up - 1
    return True


f = open('names.txt')

for line in f:
    name = line.strip()
    if is_name(name):
        print name
                
         
	       
             
             