# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:20:47 2020

@author: Ravi
"""

def strangeCounter(n):
    a = 3
    while n > a:
        n = n-a
        a *= 2
        
    return (a-n+1)
    
n=int(input())
print(strangeCounter(n))