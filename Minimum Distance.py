# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:43:28 2020

@author: Ravi
"""

def minimumDistance(arr,n):
    a = set(arr)
    if len(a) == len(arr):
        return -1
    li = {}
    for i in range(n):
        for j in range(n):
            if arr[i]==arr[j]:
                if i!=j:
                    if arr[j] not in li:
                        li[arr[j]] = j
    dist = []
    for i in li:
        x = arr.index(i)
        res = abs(x - li[i])
        dist.append(res)
    return min(dist)

n = int(input())
arr=list(map(int,input().split(" ")))
print(minimumDistance(arr,n))