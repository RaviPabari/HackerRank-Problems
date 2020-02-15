# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:01:11 2020

@author: Ravi
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def prisonerSaved(n,c,k):
    #n = number of prisoner
    #c = starting prisoner
    #k = number of sweets
    
    temp = c+k-1
    for x in range(n):
        if(temp > n):
            temp = temp -n
        else:
            return temp

print(prisonerSaved(3,3,10))