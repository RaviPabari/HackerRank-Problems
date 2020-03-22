# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:12:18 2020

@author: Ravi
"""

def magicSquare(grid):
    n = 15
    counter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i==0 and j==0:
                x = grid[i][j]
                y = grid[i+1][j+1]
                z = grid[i+2][j+2]
                if (x+y+z)!=n:
                    add = n-(x+y+z)
                    x += add
                    if 
                    
    
    return counter
    
grid = []
for i in range(3):
    arr = list(map(int,input().split(" ")))
    grid.append(arr)
print(magicSquare(grid))