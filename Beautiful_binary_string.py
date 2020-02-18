# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:30:17 2020

@author: Ravi
"""

def binary(n,s):
    return s.count('010')

n = int(input())
s = input()
print(binary(s))