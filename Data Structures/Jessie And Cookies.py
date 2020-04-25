# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:46:25 2020

@author: Ravi
"""
import heapq

def cookies(arr,k,n):
    pops = 0
    heapq.heapify(arr)
    while(arr[0]<=k and len(arr)>1):
        heapq.heappush(arr, heapq.heappop(arr)+2*heapq.heappop(arr))
        pops+=1
    return pops if arr[0]>=k else -1   
         
n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(cookies(arr,k,n))
