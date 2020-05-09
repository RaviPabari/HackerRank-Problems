# -*- coding: utf-8 -*-
"""
Created on Sun May 10 03:01:04 2020

@author: Ravi
"""
    
dic = {}
for i in range(100):
    dic[i]=[]
n = int(input())
for i in range(n):
    x = input().split()
    num = int(x[0])
    st = x[1]
    if i < n//2:
        dic[num].append('-')
    else:
        dic[num].append(st)
for i in range(100):
    if len(dic[i])>0:
        print(" ".join(dic[i]),end=" ")     
