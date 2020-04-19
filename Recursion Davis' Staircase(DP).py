# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:12:11 2020

@author: Ravi
"""

def staircaseDP(n):
    a = [0]*(n+3)
    a[1]=1
    a[2]=2
    a[3]=4
    if n==1 or n==2 or n==3:
        return a[n]
    for i in range(4,n+1):
        a[i] = a[i-1]+a[i-2]+a[i-3]
    return a[n]

t = int(input())
for i in range(t):
    n = int(input())
    print(staircaseDP(n))