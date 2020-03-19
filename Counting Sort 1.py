# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:28:01 2020

@author: Ravi
"""

def counT(arr,n):
    li = [0]*100
    for i in arr:
        li[i]+=1
    return li

n = int(input())
arr = list(map(int,input().split(" ")[:n]))
arr = counT(arr,n)
print(*arr,sep=" ")
