#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 13:55:18 2021

@author: liuqilin
"""

import re

with open('comments.txt','r',encoding="utf-8") as c:
    data = c.read()
    data = re.findall('[\u4E00-\u9FA5]',data)
    #print(data)
    
sc = open('split-comments.txt', 'w', encoding='UTF-8')
sc.write(' '.join(data))

c.close()
sc.close()

import jieba

scs = open('split-comments.txt', 'r', encoding='UTF-8')

sent = scs.read()
a = ''#空字符（中间不加空格）
d = ''
for line in sent:
    a += line.strip()#strip()是去掉每行末尾的换行符\n 1
    c = a.split()#将a分割成每个字符串 2
    b = ''.join(c)#将c的每个字符不以任何符号直接连接 3
    #print(b)
sent_list = jieba.cut(b)
for x in sent_list:
    if len(x) > 1:
        d += x
sent_list = jieba.cut(d)

sce = open('split-chinese.txt', 'w', encoding='UTF-8')
sce.write(' '.join(sent_list))

scs.close()
sce.close()