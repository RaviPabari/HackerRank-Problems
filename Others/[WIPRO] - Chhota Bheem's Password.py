# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 01:24:51 2020

@author: Ravi
"""

def kuchBhiMatlab(n,arr):
    ans = []
    if -1 in arr:
        for i in range(len(arr)):
            if arr[i]== -1:
                if arr[i-1]%2==0 and arr[i+1]%2==0:
                    arr[i] = abs(arr[i-1] - arr[i+1])
                elif arr[i-1]%2!=0 and arr[i+1]%2!=0:
                    arr[i] = abs(arr[i-1] - arr[i+1])
                else:
                    arr[i] = abs(arr[i-1] + arr[i+1])//2
        for i in range(n-1):
            if arr[i]!=1:
                ans.append(arr[i]-1)
            else:
                ans.append(arr[i])
        ans.append(arr[n-1])
        print(''.join(map(str,ans)))
    
    else:
        for i in range(n-1):
            if arr[i]!=1:
                ans.append(arr[i]-1)
            else:
                ans.append(arr[i])
        ans.append(arr[n-1])
        print(''.join(map(str,ans)))

t = int(input())
for i in range(t):
    arr = list(map(int,input().split(" ")))
    kuchBhiMatlab(arr[0],arr[1:])
