# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:39:31 2020

@author: Ravi
"""
def isWhole(n):
    if n%1==0.0:
        return True

def reverse(n):
    x = str(n)
    x = x[::-1]
    return int(x)

def isBeautifulDay(i,j,k):
    counter = 0
    for x in range(i,j+1):
        a = reverse(x)
        ans = abs(a - x)/k
        if isWhole(ans):
            counter+=1
    return counter

i,j,k = input().split()
i = int(i)
j = int(j)
k = int(k)
print(isBeautifulDay(i,j,k))
