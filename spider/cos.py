# -*- coding: utf-8 -*-
"""
Created on Sat Jul 05 16:44:54 2014

@author: shunxu
"""

number = 30

if number % 2 == 0:
    print number, "is even"
elif number % 3 == 0:
    print number,"is multiple of 3"
    

if 1:
    if 2:
        print 'A'
    else:
        print 'B'
print 'C'

import math

radius = -10
if radius >= 0:
    area = radius * radius * math.pi
print "The area is", area