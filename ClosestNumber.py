# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:28:35 2020

@author: Ravi
"""
    
def closestNumber(li):
    li.sort()
    dict = {}
    finalList = []

    for i in range(len(li)-1):
        dict[i] = abs(li[i]-li[i+1])
    liValues = list(dict.values())
    #liKeys =  list(dict.keys())
    minimum = min(liValues)
    counter = 0
#    print(liValues)
    for i in liValues:
        if i == minimum:
            counter+=1
    for i in range(0,counter):
        x = liValues.index(minimum)
        finalList.append(li[x])
        finalList.append(li[x+1])
#        print("x="+str(x))
#        print("x="+str(x+1))        
        if minimum in liValues:
#            print("yes we removed "+str(minimum))
            liValues[x]=0
#        
#    print("liValues=")
#    print(liValues)
    return finalList
        
            

n = int(input())
li = list(map(int,input().split()[:n]))
temp = closestNumber(li)
print(*temp, sep = " ")
    