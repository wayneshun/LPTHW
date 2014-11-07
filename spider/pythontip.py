# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 22:41:38 2014

@author: shunxu
"""

    
import time
import calendar



localtime = time.localtime(time.time())

print time.time()
print time.localtime()
print "Local current time :", localtime
print time.asctime()


cal = calendar.month(2014, 10)
print "Here is the calendar:"
print cal;

a,b=1,2


x = 1
y = 4

z = int(y + 10)

#c = '%.5f' % (float(a)/b)

c = '%.10f' % (float(a)/b)

d = round(float(a)/b,5)

print c,d



number = ''


for k in range(x+1,y+2):
    print k
    number = number + c[k]

print number




















