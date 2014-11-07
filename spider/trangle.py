# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 22:23:03 2014

@author: shunxu
"""
a = 3
b = 4
c = 5



l1= [a,b,c]

l2 = sorted(l1)


d = l2[0]
e = l2[1]
f = l2[2]


if d + e > f:
    if d**2 + e**2 == f**2:
        print "Z"
    elif d**2 + e**2 > f **2:
        print "R"
    else:
        print "D"      
else:
    print "W"