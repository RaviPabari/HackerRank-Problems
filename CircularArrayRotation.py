#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:15:40 2020

@author: ravi
"""

n,k,q = map(int, input().split(" "))
arr = list(map(int , input().split(" ")[:n]))
#arr = arr[-k:]+arr[:-k] does not work for higher values of k
arr = arr[n-(k%n):n] + arr[0:n-(k%n)]
print(arr)
for i in range(q):
    x = int(input())
    print(arr[x])