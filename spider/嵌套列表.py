# -*- coding: utf-8 -*-
"""
Created on Tue Aug 05 20:17:59 2014

@author: shunxu
"""

students = [['Zhang',60],['Wang',90],['Li',81],['Xu',100]]

print float(sum([student[1] for student in students])) / len(students)