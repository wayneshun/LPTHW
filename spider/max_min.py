# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 20:54:22 2014

@author: shunxu
"""

def max_min(lst):
    max = min = lst[0]
    for i in lst:
        if max < i:
            max = i
        if min > i:
            min = i
    return max,min



words = ['abcd','ab','defghi']

lst = []

for word in words:
    lst.append((len(word),word))
    
lst.sort(reverse = True)

sort_words = []

for e in lst:
    length,word =  e  #元组赋值
    sort_words.append(word)

print sort_words












































    
