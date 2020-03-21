# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:03:38 2020

@author: Ravi
"""

def CountSort(arr,n):
    count = [0]*100
    for i in arr:
        count[i]+=1
    i=0
    for a in range(100):
        for c in range(count[a]):
            arr[i] = a
            i+=1
    return arr