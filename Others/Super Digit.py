#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:19:00 2020

@author: ravi
"""


def superdigit(n):
    if int(n)//10==0:
        print(n)
        return
    else:
        x = list(map(int,n))
        s = sum(x)
#        print(s)
        superdigit(str(s))
        
#n,k = input().split()
#n = n*int(k)
#print(n)
#superdigit(n)    
n, k = map(int, input().split())
x = n*k%9
print(x if x else 9)

#x=12
#if x:
#    print(x)
#else:
#    print(9)