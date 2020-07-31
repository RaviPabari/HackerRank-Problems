#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 18:56:40 2020

@author: ravi
"""

def largestBruteForce(arr):
    maxArea = 0
    for i in range(len(arr)):
        count = 1
        l=i
        r=i
        m=arr[i]
        l1=True
        r1=True
#        print("m=",m)
        while(l1==True or r1==True):
            if l1 is True:
                l-=1
            if r1 is True:
                r+=1
            if l>=0:
                if arr[l]>=m:
                    count+=1
                else:
                    l1=False
            else:
                l1=False
            if r<len(arr):
                if arr[r]>=m:
                    count+=1
                else:
                    r1=False
            else:
                r1=False
            if r>len(arr) and l<=0:
                break
#        print("count=",count)
        temp = count*m
#        print("temp=",temp)
        if temp>maxArea:
            maxArea=temp
#        print("maxArea=",maxArea)
#        print("----")
    return maxArea
        

n = int(input())
arr = list(map(int,input().split()))
print(largestBruteForce(arr))