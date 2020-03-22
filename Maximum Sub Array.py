# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 00:27:55 2020

@author: Ravi
"""

def maxSubarr(arr):
    #using kadane's Algo TY kadane
    max_current = max_global = arr[0]
    for i in range(1,len(arr)):
        max_current = max(arr[i], max_current+arr[i] )
        if max_global < max_current:
            max_global = max_current
    
    arr.sort()
    
    a = b = arr[0]
    for i in range(1,len(arr)):
        a = max(arr[i],a+arr[i])
        if b < a:
            b = a
    print(str(max_global)+" "+str(b))


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split(" ")[:n]))
    maxSubarr(arr)
