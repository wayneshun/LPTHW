# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 22:53:49 2014

@author: shunxu
"""


"""def gcd(a,b):
    if a < b:
        a,b = b,a
    while b:
        a,b=b,a%b
    return a
"""
    
"""a = 2
b = 5    
  
#print a*b/gcd(a,b)

for i in range(1,a*b+2):
    if i % a == 0 and i % b == 0:
        print i
        break
"""



L=[3,5,10]

def LCM(a,b):
    c = a
    d = b
    while b != 0:
        temp = a % b
        a = b;
        b = temp
    return c * d / a

print reduce(LCM,L)