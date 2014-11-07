# -*- coding: utf-8 -*-
"""
Created on Sat Jul 05 20:28:09 2014

@author: shunxu
"""

for i in range(1, 3):
    for j in range(1, 3):
        if i * j < 2:
            break
        print i * j