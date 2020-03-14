# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 22:44:56 2020

@author: Ravi
"""

def winner(arr,jack):
    p1 = 'Player 1 wins'
    p2 = 'Player 2 wins'
    d = 'Draw'
    
    if arr[0] == jack and arr[2]!= jack:
        return p1
    
    if arr[0]!= jack and arr[2]== jack:
        return p2
    
    if arr[0]!=jack and arr[0]!=jack:
        if arr[1] == arr[3]:
            return d
    
    if arr[0]!=jack and arr[0]!=jack:
        if arr[1]>arr[3]:
            return p1
        else:
            return p2
        
    if arr[0] == jack and arr[2]==jack:
        if arr[1]>arr[3]:
            return p1
        else:
            return p2
        
    if arr[0] == jack and arr[2]==jack:
        if arr[1] == arr[3]:
            return d
    
    if arr[0] == arr[2]:
        if arr[1]>arr[3]:
            return p1
        else:
            return p2
    
jack = input()
n = int(input())
arr = []
for i in range(n):
    arr = list(map(str , input().split(" ")))
    print(winner(arr,jack))