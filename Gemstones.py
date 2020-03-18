# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:21:28 2020

@author: Ravi
"""

        
n = int(input())
res = set(input())
for i in range(n-1):
    a = input()
    res = res.intersection(a)
print(len(res))