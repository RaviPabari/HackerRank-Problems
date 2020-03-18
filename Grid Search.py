# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:44:31 2020

@author: Ravi
"""

def gridSearch(grid,pattern):  
    r = len(grid)
    c = len(grid[0])
    R = len(pattern)
    C = len(pattern[0])
    for i in range(r-R+1):
        for j in range(c-C+1):
            flag = True
            for ii in range(R):
                for jj in range(C):
                    if flag:
                        flag = (grid[i+ii][j+jj]==pattern[ii][jj])
                    else:
                        break
                if not flag:
                    break
            if flag:
                return 'YES'
    return 'NO'

t = int(input())
for i in range(t):
    r,c = map(int , input().split(" "))
    grid = []
    for i in range(r):
        grid.append(input())
    pattern = []
    R,C = map(int,input().split(" "))
    for i in range(R):
        pattern.append(input())
    print(gridSearch(grid,r,c,pattern,R,C))