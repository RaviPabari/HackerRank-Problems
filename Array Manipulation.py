# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:48:37 2020

@author: Ravi
"""


n,m = map(int,input().split(" "))
arr = [0]*n
for i in range(m):
    mx = 0
    a,b,k = map(int,input().split(" "))
    for i in range(a,b+1):
        arr[i-1]+=k
        if arr[i-1]>mx:
            mx =arr[i-1]
print(arr)