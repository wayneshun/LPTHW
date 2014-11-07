# -*- coding: utf-8 -*-
"""
Created on Sat Jul 05 16:01:48 2014

@author: shunxu
"""
n = int(raw_input("number:"))

x = (n / 3600)
y = ((n % 3600) / 60)
z = ((n % 3600) % 60)

print x, y, z
