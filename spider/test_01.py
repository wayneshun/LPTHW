# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 21:45:27 2014

@author: shunxu
"""

line = '0100100011101'

def read_line(line):
    dict = {}
    n = len(line)
    for i in range(n):
        if line[i] == "1":
            dict[i] = 1
    print dict

read_line(line)      


#方法一
def read_line(line):
    sample = {}
    n = len(line)
    for i in range(n):
        if line[i]!='0':
            sample[i] = int(line[i])
    return sample
 
#方法二
def xread_line(line):
    return((idx,int(val)) for idx, val in enumerate(line) if val != '0')
 
print read_line('0001110101')
print list(xread_line('0001110101'))


l = "hello world"
for k,v in enumerate(l):
    if 
    print (k,v),

  