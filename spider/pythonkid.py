# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 14:30:20 2014

@author: shunxu
"""
#格式化字符串
print "hello world"
print "hello \nworld"
print "123\t456"
print "1234\t567"
name = 'waynexu'
print 'My name is %s' % name
print 'I am %i years old' % 25
print 'I am %.2f m tall' % 1.73

#join 和 split
a = "jim,kate,jane,ross,jolin,jay,wayne,david"
print a.split(',')

list = ['my','name','is','wayne']
print " ".join(list)

#开头结尾
text='welcome to qttc blog'
print text.startswith('w')      # True
print text.startswith('wel')    # True
print text.startswith('c')      # False
print text.startswith('')       # True
print text.endswith("blog")


#查询和索引
#in 
#index()

#删除
print name.strip("xu")
name2 = "wayne                "
print name2.strip()

#大小写
string1 = "Hello"
string2 = string1.lower()
print string2

string3 = string2.upper()
print string3

file = open('note.txt','r')
line = file.readline()
print line











