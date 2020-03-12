#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:53:34 2020

@author: ravi
"""
def FunnyOrNot(s):
    li1=[]
    diff = []
    for i in range(len(s)):
        li1.append(ord(s[i]))
    for i in range(len(li1)-1):
        diff.append(abs(li1[i]-li1[i+1]))
    return 'Funny' if diff == diff[::-1] else 'Not Funny'
        
n = int(input())
for i in range(n):
    s = input()
    print(FunnyOrNot(s))