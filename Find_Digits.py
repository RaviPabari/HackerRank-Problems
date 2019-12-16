#25points | Easy
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:16:48 2019

@author: Ravi
"""

def convertToList(n):
    z = str(n)
    list = []
    for i in z:
        list.append(i)
    return findDigit(list,n)

#newlist = finddigits(1012)

def findDigit(list,n):
    count = 0
    for i in list:
        if int(i)!=0:
            if n%int(i)==0:
                count+=1
            
    print(count)
    
n = int(input())
while n>0:
    x =int(input())
    convertToList(x)
    x-=1


            
