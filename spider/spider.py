# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 12:07:26 2014

@author: shunxu
"""
import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.htm' % x)
        x += 1

html = getHtml("http://tech.qq.com/")

print getImg(html)

