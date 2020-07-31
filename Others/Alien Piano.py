#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:13:30 2020

@author: ravi
"""
def alienPiano(arr):
    rulebreak=0
    asc = False
    dsc = False
    ac = 4
    dc = 4
    for i in range(len(arr)-1):
        if arr[i]>=arr[i+1]:
            asc = True
        if arr[i]<=arr[i+1]:
            dsc = False
        if asc:
            if arr[i]>=arr[i+1]:
                ac-=1
                if ac<=0:
                    ac=4
        if dsc:
            if arr[i]<=arr[i+1]:
                dc-=1
                if dc<=0:
                    dc=4
        if asc:
            if dc<4:
                rulebreak+=1
                dc=4
                asc=False
        if dsc:
            if ac<4:
                rulebreak+=1
                dc=4
                dsc=False
    return rulebreak
            
            
        
        
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = alienPiano(arr)
    print("Case #"+str(i+1)+":",str(ans))