# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:32:14 2020

@author: Ravi
"""
from collections import Counter

def isValid(s): 
    s1 = Counter(s) 
    values = list(s1.values()) 
    val_max = max(values) 
    val_min = min(values) 
    if val_max == val_min or (val_max - val_min == 1 and values.count(val_max) == 1) or (val_min == 1 and values.count(val_min) == 1 and len(set(values))==2) : 
        return 'YES' 
    else: 
        return 'NO'

s = input()
print(isValid(s