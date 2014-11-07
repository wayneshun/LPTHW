# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 16:13:46 2014

@author: shunxu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 11:20:43 2014

@author: shunxu
"""

import math
  
   
  
num_range_low = 0  
num_range_high = 100  
real_num = 0  
  
remain_guess_times = 0  

print  int(math.ceil(math.log(4,2)))



remain_guess_times = int(math.ceil(math.log(num_range_high - num_range_low + 1, 2)))  

print remain_guess_times

print("-----------math functions-------------")  
#数学函数  
#取顶  
print(math.ceil(2.3))  
#取底  
print(math.floor(2.3))  
#取绝对值  
print(math.fabs(-1))  
#阶乘  
print(math.factorial(3))  
#求直角三角形斜边长  
print(math.hypot(3,4))  
#求x的y次方  
print(math.pow(2,3))  
#求x的开平方  
print(math.sqrt(4))  
#截断，只取整数部分  
print(math.trunc(2.3))  
#判断是否NaN(not a number)  
print(math.isnan(2.3333)) 