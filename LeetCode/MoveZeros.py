#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:05:04 2020

@author: ravi
"""
def TwoPointer(arr):
    p1 = 0  #points to non-zero 
    p2 = 0  #points to zeros
    i=0
    while(i!=(len(arr)-1)):
        while(True):
            if p1>= len(arr):
                break
            if arr[p1]!=0:
                break
            else:
                p1+=1
                i+=1
        while(True):
            if p2>=len(arr):
                break
            if arr[p2]==0:
                break
            else:
                p2+=1
        if p1 < len(arr) and p2 < len(arr):
            if p1>p2:
                arr[p1],arr[p2] = arr[p2],arr[p1]
            else:
                p1 = p2
        else:
            break
    print(arr)
    
arr = list(map(int,input().split()))
TwoPointer(arr)