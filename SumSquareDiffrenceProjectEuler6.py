# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:25:14 2020

@author: Ravi
"""

def calculator(a):
    #for (1+2+3...n)^2
#    linear = (a*(a+1)//2)**2
#    #for square (1^2 + 2^2 + ....n^2)
#    square = a*(a+1)*(2*a+1)//6
    return ((a*(a+1)//2)**2 - a*(a+1)*(2*a+1)//6)
    

n = int(input())
for i in range(n):
    x = int(input())
    print(calculator(x))