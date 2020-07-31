#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 10:49:34 2020

@author: ravi
"""

def recordBreaker(arr):
    peak = 0
    cmax = float("-inf")
    if len(arr)==0:
        return 0
    if len(arr)==1:
        return 1
    for i in range(len(arr)):
        if i==0:
            if arr[i]>arr[i+1]:
                if arr[i]>cmax:
                    cmax=arr[i]
                    peak+=1
        if i>0 and i<len(arr)-1:
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                if arr[i]>cmax:
                    cmax = arr[i]
                    peak+=1
        if i==len(arr)-1:
            if arr[i]>arr[i-1]:
                if arr[i]>cmax:
                    cmax = arr[i]
                    peak+=1
    return peak

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = recordBreaker(arr)
    print("Case #"+str(i+1)+":",str(ans))