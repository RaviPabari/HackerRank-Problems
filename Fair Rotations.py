# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:26:00 2020

@author: Ravi
"""

def fairRotations(arr,n):
    sum = 0
    for i in range(n):
        sum+=n
    if sum%2!=0:
        return 'NO'
    else:
        counter = 0
        for i in range(n):
            if arr[i]%2!=0:
                arr[i]+=1
                arr[i+1]+=1
                counter+=2
        return counter
                

n = int(input())
arr = list(map(int,input().split(" ")[:n]))
print(fairRotations(arr,n))