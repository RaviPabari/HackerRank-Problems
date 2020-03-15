# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:18:08 2020

@author: Ravi
"""

def loss(s):
    k = 'SOS'
    counter = 0
    for i in range(0,len(s)):
        if s[i]!=k[i%len(k)]:
            counter+=1
    print(counter)

s = input()
loss(s)
