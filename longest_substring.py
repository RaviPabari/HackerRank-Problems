# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 23:37:29 2020

@author: Ravi
"""

def longest(s):
    a = 0
    b = 0
    freq = {}
    max = 0
    while b < len(s):
        if s[b] not in freq:
            freq[b] = s[b]
            b+=1
            max = len(freq)
        else:
            freq.pop(s[a])
            a+=1
    return max
s = input()
print(longest(s))
            