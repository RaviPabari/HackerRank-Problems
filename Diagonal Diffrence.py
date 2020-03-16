# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:11:52 2020

@author: Ravi
"""
def DiagonalDiffrence(grid,n):
    right = 0
    left = 0
    final = []
    for i in range(n):
        for j in range(n):
            if i==j:
                right+=grid[i][j] 
                print(grid[i][j])
    print("right = ",str(right))
    for i in grid:
        final.append(i[::-1])
    for i in range(n):
        for j in range(n):
            if i==j:
                left += final[i][j]
                print(final[i][j])
#    print("left",str(left))                
    return abs(right - left)
    


#n = int(input())
#n = 3
grid = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

#for i in range(n):
#    x = list(map(int,input().split(" ")[:n]))
#  grid.append(list(map(int,input().split(" ")[:n])))  
print(DiagonalDiffrence(grid,n))