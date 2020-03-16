# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:34:17 2020

@author: Ravi
"""

def cavityMap(grid,n):
    if n<3:
        return grid
    final = grid[:]
    for i in range(1,n-1):
        for j in range(1,n-1):
            if grid[i][j]>max(grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]):
                temp = list(final[i])
                temp[j] = 'X'
                s = ''
                for v in temp:
                    s+=v
                final[i]=s
    return final

n = int(input())
grid = []
for i in range(n):
    grid.append(input())
g = cavityMap(grid,n)
for i in g:
    print(i)