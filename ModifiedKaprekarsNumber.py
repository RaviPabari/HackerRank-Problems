#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:18:26 2020

@author: ravi
"""
li = []
def kaprekar(n):
    if n == 1:
        li.append(n)
    if n>=2 and n < 10:
        q = n**2
        q = str(q)
        l = len(q)
        if l>=2:
            q = n**2
            q = str(q)
            l = len(q)
            x = l//2
            temp1 = ""
            temp2 = ""
            temp1 = temp1 + q[:x]
            temp2 = temp2 + q[x:l]
            temp1 = int(temp1)
            temp2 = int(temp2)
            add = temp1+temp2
            if add == n:
                li.append(n)
    if n>=10:
        q = n**2
        q = str(q)
        l = len(q)
        x = l//2
        temp1 = ""
        temp2 = ""
        temp1 = temp1 + q[:x]
        temp2 = temp2 + q[x:l]
        temp1 = int(temp1)
        temp2 = int(temp2)
        add = temp1+temp2
        if add == n:
            li.append(n)

p = int(input())
q = int(input())
for i in range(p,q+1):
    kaprekar(i)
if len(li)!=0:
    print(*li,sep = " ")
else:
    print("INVALID RANGE")
    