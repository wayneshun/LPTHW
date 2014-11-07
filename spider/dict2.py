# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 14:13:38 2014

@author: shunxu
"""

def revert_dict(d):
    reverse = {}
    for k,v in d.items():
        if v in reverse:
            reverse[v].append(k)
        else:
            reverse[v] = [k]
    return reverse

d = {'A':28,'B':25,'C':25}

t = revert_dict(d)
print t