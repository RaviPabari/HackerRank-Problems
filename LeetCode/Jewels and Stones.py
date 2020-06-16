# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:38:32 2020

@author: Ravi
"""
from collections import Counter
def jewls(s,j):
    x = Counter(s)
    j = set(j)
    total = 0
    for i in j:
        total += x[i]
    return total

s = input()
j = input()
print(jewls(s,j))
