# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:08:43 2020

@author: Ravi
"""
from itertools import combinations
def acmTeam(topic,n):
    maxTeam = 0
    maxKnownTopic = 0
    comb = combinations(topic,2)
    for i in comb:
        n = bin(((int(i[0],2) | int(i[1],2)))).count('1')
        if maxKnownTopic < n:
            maxKnownTopic = n
            maxTeam = 1
        elif n == maxKnownTopic:
            maxTeam +=1
    return maxTeam , maxKnownTopic

n,m = map(int, input().split(" "))
li = []
for i in range(n):
    li.append(input())
team , top = acmTeam(li,m)
print(top)
print(team)
