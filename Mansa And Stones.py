# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:31:31 2020

@author: Ravi
"""
#ans = []
#def lastStones(n,a,b,stoneValue):
#    if n==1:
#        ans.append(stoneValue)
#        return
#    lastStones(n-1,a,b,stoneValue+a)
#    lastStones(n-1,a,b,stoneValue+b)
#    return ans
def lastStones(n,a,b):
    s = set()
    for i in range(n):
        s.add((b*i)+(a*(n-i-1)))
    return list(s)

t = int(input())
for i in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    s = lastStones(n,a,b)
    s.sort()
    print(*s,sep=' ')