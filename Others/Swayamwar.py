#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:13:21 2020

@author: ravi
"""


def Swayamvar(b,g,n):
    b = list(b)
    g = list(g)
    count = n
    down = n
    i=0
    while(down!=0):
#       print(b)
#       print(g)
#       print("count=",str(count))
#       print("down=",str(down))
#       print("---")
       if count==0:
           break
       if  b[i]==g[i]:
           down-=1
           b.pop(i)
           g.pop(i)
           count = down
       else:
           count-=1
           temp = g.pop(i)
           g.append(temp)
    return down

n = int(input())
b,g = input().split()
print(Swayamvar(b,g,n))