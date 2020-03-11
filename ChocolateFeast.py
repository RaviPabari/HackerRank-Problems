# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:37:05 2020

@author: Ravi
"""

def freeChocolate(n,c,w):
    total = n//c
    wrap = total
    while(wrap>=w):
        wrap = wrap - w
        total += 1
        wrap += 1
    return total

n = int(input())
for i in range(n):
    a,b,c = map(int , input().split())
    print(freeChocolate(a,b,c))