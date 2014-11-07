# -*- coding: utf-8 -*-
"""
Created on Sat Jul 05 18:56:32 2014

@author: shunxu
"""

num = 1
Total_num = 3
count = 0

while (num <= Total_num):
    grade = input("input NO."+str(num)+" student\'s grade:")
    if (grade >= 60):
        count = count + 1
    else:
        pass
    num = num + 1
print "Passed student number is", count