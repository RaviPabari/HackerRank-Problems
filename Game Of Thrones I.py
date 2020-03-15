# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:58:26 2020

@author: Ravi
"""
from collections import Counter
def gameOfThrones(s):
    odd = 0
    se = Counter(s)
    for i in se.values():
        if i%2!=0:
            odd+=1
        if odd>1:
            return 'NO'
    return 'YES'
    
s = input()
print(gameOfThrones(s))