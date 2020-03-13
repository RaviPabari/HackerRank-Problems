# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:32:14 2020

@author: Ravi
"""
from collections import Counter

def SherlocksValidString(s):
    dic = dict(Counter(s))
    val = list(dic.values())
    val = dict(Counter(val))
    print(dic)
    print(val)
    val_key = list(val.keys())
    print(val_key)
    abc = list(val.values())
    print(abc)
    a = max(abc)    
    indx = abc.index(a)
    a = val_key[indx]
    print(a)
    if len(val) == 1:
        return "YES"
    counter = 1
    for i in dic:
        if counter < 0:
            return "NO"
        if dic[i] != a:
            if abs(dic[i]-a) == 1:
                counter -=1
    return "YES"
s = input()
print(SherlocksValidString(s))