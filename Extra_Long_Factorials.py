#Hackerrank Problem Solving : Medium : 20 points : Problem --> Extra Long Factorials

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:03:41 2019

@author: Ravi
"""
#with the help of Dictionary we can solve this easily AF in very less time

def efficient_fact(n,d):
    if n in d:
        return d[n]
    else:
        ans = n*efficient_fact(n-1,d)
        d[n]=ans
        return ans
   
d ={0:1,1:1}
n=int(input())
print(efficient_fact(n,d))
