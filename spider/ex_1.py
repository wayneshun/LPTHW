# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 22:15:58 2014

@author: shunxu
"""
def multiple(a,b):
    x= a*b
    print '{0:' '>10}'.format(a)
    print 'x'+'{0:' '>9}'.format(b)
    print  '{0:''-' '>10}'.format('-')
    print  '{0:' '>10}'.format(x)
    print  '{0:''*''>20}'.format('*')


#multiple(a,b)

print '{:>8}'.format('189')
print '{:0>8}'.format('189')
print '{0:' '>8}'.format('189')

t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}

print ("{:0>4}-{:0>2}-{:0>2} {:0>2}:{:0>2}:{:0>2}".format(t['year'], t['month'], t['day'],t['hour'],t['minute'],t['second']))

print ("{:0>4}-{:0>2}-{:0>2} {:0>2}:{:0>2}:{:0>2}".format(t['year'], t['month'], t['day'], t['hour'], t['minute'], t['second']))


print max(1,2,3)

l1= [1,2,3]
l2 = sorted(l1)
print l2