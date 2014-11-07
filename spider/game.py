# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 17:32:15 2014

@author: shunxu
"""

import re

f = open("names.txt")

pattern = 'C.A'

for line in f:
    name = line.strip()
    result = re.search(pattern,name)
    if reslut:
        print name

f.close()
    
    