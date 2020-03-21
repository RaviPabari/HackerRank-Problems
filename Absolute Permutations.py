# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:26:24 2020

@author: Ravi
"""

def absoulutePermutation(n,k):
    if k==0:
        return list(range(1,n+1))
    elif (n/k)%2!=0:
        return [-1]
    else:
        add = True
        posi = []
        for i in range(1,n+1):
            if add:
                posi.append(i+k)
            else:
                posi.append(i-k)
            
            if i%k==0:
                if add:
                    add =False
                else:
                    add = True
    return posi
        
t = int(input())
for i in range(t):
    n,k = map(int,input().split(" "))
    posi = absoulutePermutation(n,k)
    print(*posi,sep=" ")
