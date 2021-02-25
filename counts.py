#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:39:53 2021

@author: liuqilin
"""

import json
def getText():
    txt = open('split-chinese.txt', 'r', encoding='UTF-8').read()
    return txt
    
hamletTxt = getText()
words = hamletTxt.split()                            #以空格为分割，将字符串转换为列表
counts = {}                                          #建立空字典
for word in words:                                   #get() 函数返回指定键的值，如果值不在字典中返回默认值。
    counts[word] = counts.get(word,0)+1              #字典格式生成,字典的键与指定值的写入
items = list(counts.items())                         #字典列表转换：[(key:data),(key1:data1)]
items.sort(key=lambda x: x[1], reverse=True)         #sort() 函数用于排序，lambda一种函数定义，类似def
#print(items)

countList = []
for i in range(len(items)):
    countDict = {}
    word, count = items[i]
    if count >= 10:
        countDict['name'] = word
        countDict['value'] = count
        countList.append(countDict)
# print(countList)
All = {}
All['All'] = countList
#print(All)

file = open('comments.json','w',encoding='UTF-8')
json.dump(All,file,ensure_ascii=False)