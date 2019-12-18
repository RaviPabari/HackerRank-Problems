# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 11:47:27 2019

@author: Ravi
"""
import math


def encrypt(s):
    s = s.replace(" ","")
    length = len(s)
    n = math.sqrt(length)
    row = math.floor(n)
    col = math.ceil(n)
    if row*col < len(s):
        row = col
    ans =''
    for i in range(col):
        for j in range(row):
            if(i+j*col < len(s)):       
                ans = ans + s[i+j*col]
        ans = ans +" "
    return ans
s = input()
print(encrypt(s))
    
    
