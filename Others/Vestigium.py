# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:46:44 2020

@author: Ravi
"""
t = int(input())
counter = 1
for i in range(t):
    grid = []
    n = int(input())
    for j in range(n):
        arr = list(map(int,input().split()))
        grid.append(arr)
    k = 0
    c = 0
    r = 0
    for a in range(n):
        k += grid[a][a]
    for b in grid:
        x = set(b)
        if len(x)<len(b):
            r+=1
    for row in range(n):
        li = []
        for col in range(n):
            li.append(grid[col][row])
        x = set(li)
        if len(x)<len(li):
            c+=1   
    print("Case #"+str(counter)+": "+str(k)+" "+str(r)+" "+str(c))
    counter+=1