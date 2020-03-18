# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:09:37 2020

@author: Ravi
"""
def maximizeXOR(a,b):
    res = []
    for i in range(a,b+1):
        for j in range(i,b+1):
            res.append(i^j)
    return max(res)

a = int(input())
b = int(input())
print(maximizeXOR(a,b))