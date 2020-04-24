# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:26:17 2020

@author: Ravi
"""

def nestingDepth(s):
    x = 0
    i = 0
    new = ''
    while(x<len(s)):
        if s[x]=='1':
            new+='('
            while(s[i]!='0' or i==len(s)):
                new+='1'
                x+=1
                i+=1
                if i==len(s):
                    break
            new+=')'
        else:
            new+='0'
            x+=1
            i+=1
    return new

t = int(input())
counter = 1
for i in range(t):
    s = input()
    nestedStr = nestingDepth(s)
    print("Case #"+str(counter)+": "+nestedStr)
    counter+=1