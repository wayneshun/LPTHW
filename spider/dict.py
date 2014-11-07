# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 11:37:16 2014

@author: shunxu
"""

count = {}

for i in 'applause':
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

print count


f = open("emma.txt")

count2 = {}

for i in f:
    i = i.strip()
    words = i.split()
    for word in words:
        if word in count:
            count2[word] += 1
        else:
            count2[word] = 1

word_freq = []
for word in count:
    word_freq.append((count[word],word))

word_freq.sort(reverse = True)

for freq,word in word_freq[:10]:
    print word,freq







