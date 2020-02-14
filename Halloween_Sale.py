# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:31:34 2020

@author: Ravi
"""
def sale(p,n,m,s):

    total = 0
    counter = 0
    temp = p
    for i in range(s):
        if total<=s:
            total += temp
            if(total >=s):
                break
            counter +=1
            temp = temp-n
            if temp <= m:
                temp = m
    print(counter)
            
p,n,m,s = map(int, input().split())
sale(p,n,m,s)