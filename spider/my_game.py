# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 21:33:19 2014

@author: shunxu
"""

import random

choices = ['rock', 'Spock', 'paper', 'lizard', 'scissors']

comp_name = random.choice(choices)
    
print comp_name

print random.random()
print random.uniform(1,5)

print random.choice("学习Python") 
print random.choice(["JGood", "is", "a", "handsome", "boy"])
print random.choice(("Tuple", "List", "Dict"))