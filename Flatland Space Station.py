# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:45:19 2020

@author: Ravi
"""
#still teestcase-9 fails
#90 17
#4 76 16 71 56 7 77 31 2 66 12 32 57 11 19 14 42
def spaceStation(n,m,arr):
    if n==m:
        return 0
    arr.sort()
    arr.insert(0,0)
    arr.append(n-1)
    diff = []
    for i in range(len(arr)-1):
        diff.append(arr[i+1]-arr[i])
    x = max(diff)
    ind = diff.index(x)
    if (ind+1 == len(diff)):
        return x
    if (ind == 0):
        return x
    else:
        return x//2

n,m = map(int,input().split(" "))
arr = list(map(int,input().split(" ")[:m]))
print(spaceStation(n,m,arr))
