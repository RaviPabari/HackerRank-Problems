# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:32:54 2020

@author: Ravi
"""

def cout(arr,k,n):
    e = 100
    current = 0
    tempCurrent = None
    while(tempCurrent!=0):
        i = arr[(current+k)%n]
        if i==0:
            e = e-1
        else:
            e = e-3
        tempCurrent = (current+k)%n
        current+=k
    print(e)
n,k = map(int,input().split())
arr = list(map(int,input().split()))
cout(arr,k,n)