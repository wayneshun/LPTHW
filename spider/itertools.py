# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 22:04:53 2014

@author: shunxu
"""

import itertools

list1 = ['a','b','c']
list2 = ['11','12','13']

for item in itertools.chain(list1,list2):
    print item

"""
for item in itertools.cycle(list1):
    print item,
"""

i = 0
for item in itertools.count(100):
    if i > 10:
        break
    print item,
    i = i + 1
    
s = "abcd"

a = itertools.permutations(s)
a = sorted(list(set(a)))
for i in a:
    print ''.join(i)