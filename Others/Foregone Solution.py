# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:43:45 2020

@author: Ravi
"""

def solution(n):
    s =''
    for i in n:
        if i=='4':
            s+='3'
        else:
            s+=i
    n = int(n)
    s = int(s)
    ans = n-s
    return ans,s
t = int(input())
for i in range(1,t+1):
    n = input()
    a,b = solution(n)
    print("Case "+"#"+str(i)+": "+str(a)+" "+str(b))
