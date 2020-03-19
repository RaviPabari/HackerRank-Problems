# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:21:39 2020

@author: Ravi
"""
from collections import Counter
def Anagram(s):
    if len(s)%2!=0:
        return -1
    else:
        """
        remove the common and the remaining no of chars will be the ans to make the              strings anagram
        """
        a1 = Counter(s[:len(s)//2])
        a2 = Counter(s[len(s)//2:])
        diff = a1-a2
        return sum(diff.values())
        
        

n = int(input())
for i in range(n):
    s = input()
    print(Anagram(s))