# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:21:06 2020

@author: Ravi
"""

def MazeRunner(n,s):
    ans = ''
    for i in s:
        if i=='S':
            ans+='E'
        else:
            ans+='S'
    return ans

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    ans = MazeRunner(n,s)
    print("Case "+"#"+str(i)+": "+str(ans))