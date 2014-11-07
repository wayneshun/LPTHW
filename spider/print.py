# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 21:37:09 2014

@author: shunxu
"""

def spiral_number(N):
    step_x = [0, 1, 0, -1]
    step_y = [1, 0, -1, 0]
    a = [[0 for j in xrange(N)] for j in xrange(N)]
    dir = 0
    i = 0
    j = 0
    a[i][j] = 1
    n = 2
    while n <= N ** 2:
        x = i + step_x[dir]
        y = j + step_y[dir]
        if x >= 0 and x < N and y >= 0 and y < N and a[x][y] == 0:
            a[x][y] = n
            n += 1
            i = x
            j = y
        else:
            dir = (dir + 1 + len(step_x)) % len(step_x)
        
    for i in xrange(N):
        for j in xrange(N):
            print a[i][j], '\t',
        print

spiral_number(4)

print "Number\tSquare\tCube"  
for i in range (1, 11):  
    print i,'\t',i**2,'\t',i**3 