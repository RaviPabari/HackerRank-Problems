# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 02:17:45 2020

@author: Ravi
"""

def palindromeIndex(s):
    n = len(s)
    for i in range(n//2):
        if s[i]!= s[n-i-1]:
            if s[i]==s[n-i-2] and s[i+1] == s[n-i-3]:
                return n-i-1
    return -1

n = int(input())
for i in range(n):
    s = input()
    print(palindromeIndex(s))