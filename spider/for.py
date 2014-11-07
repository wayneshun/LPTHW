# -*- coding: utf-8 -*-
"""
Created on Sat Jul 05 19:57:13 2014

@author: shunxu
"""

count = 0

for num in range(1,4):
    grade = input("input NO."+str(num)+" student\'s grade:")
    if (grade>=60):
        count = count + 1
    else:
        pass

print "Total number of passed student is ", count
