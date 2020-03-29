# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 01:52:02 2020

@author: Ravi
"""

def PerryThisIsForYouMyFriend(arr,n):
    index = []
    prev = n*n-n+1
    index.append(prev)
    counter = 1
    for i in range(n-1):
        if counter < n//2+1 :
            prev = prev - 2*n + 1
            index.append(prev)
            counter+=1
        else:
            counter+=1
            prev = prev + 2*n +1
            index.append(prev)
    finalLi = []
    for i in index:
        finalLi.append(arr[i-1])
    encrypted_msg = ''
    for i in finalLi:
        encrypted_msg += chr(96+(i%26))
    print(encrypted_msg)
t = int(input())
for i in range(t):
    arr = list(map(int,input().split(" ")))
    PerryThisIsForYouMyFriend(arr[2:],arr[0])