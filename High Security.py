# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:59:14 2020

@author: Ravi
"""

def HighSec(s,d):
    total= 0
    for i in s:
        total += (ord(i) - 97 + d)%26
    print(total)
    
s = input()
d = int(input())
HighSec(s,d)