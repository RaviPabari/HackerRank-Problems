# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:35:12 2020

@author: Ravi
"""
def permuT(arr,crr,n,k):
    arr.sort()
    crr.sort(reverse = True)
    counter = 0
    for i in range(n):
        if arr[i]+crr[i]>=k:
            counter+=1
    if counter==n:
        return 'YES'
    else:
        return 'NO'

                    
    
    

q = int(input())
for i in range(q):
    n,k = map(int,input().split(" "))
    arr = list(map(int,input().split(" ")))
    crr = list(map(int,input().split(" ")))
    print(permuT(arr,crr,n,k))