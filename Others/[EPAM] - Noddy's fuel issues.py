# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:38:50 2020

@author: Ravi
"""

def fuelSituation(arr,n,f,k):
    if f<k:
        return 'No'
    fuel = 0
    if k==1:
        if n<f:
            return 'No'
    for i in range(len(arr)):
            if arr[i]<=k:
                fuel+=arr[i]
            if fuel==f:
                return 'Yes'
    return 'No'
            

t = int(input())
for i in range(t):
    arr = list(map(int,input().split(" ")))
    f = int(input())
    k = int(input())
    print(fuelSituation(arr[1:],arr[0],f,k))