# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:17:09 2020

@author: Ravi
"""

def idkName(n):
    count = bin(n).count('0')-1
    return count

n=int(input())
print(idkName(n))