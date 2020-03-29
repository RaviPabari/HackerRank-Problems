# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:11:05 2020

@author: Ravi
"""
"""
Created on Mon Mar 23 14:11:05 2020

@author: Ravi
"""
import sys
def battle(a,b,n):
    counter = 0
    a.sort()
    b.sort()
    for i in range(n):
        for j in range(n):
            if a[i]>b[j]:
#                print(str(a[i]),"-->",str(b[j]))
                counter+=1
                b[j]=sys.maxsize
#                print(a)
#                print(b)
                break
        
    return counter


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split(" ")[:n]))
    b = list(map(int,input().split(" ")[:n]))
    print(battle(a,b,n))