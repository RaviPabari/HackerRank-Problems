# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:19:56 2020

@author: Ravi
"""
import math
def special(x,d,n):
    specialCounter = 0
    xi = []
    for i in x:
        coun = 0
        for j in range(1,int(i)+1):
            xi.append(j)
            coun +=1
        ac = math.ceil(int(i)/d)
        if coun != ac*d:
            remains = ac*d - coun
            for k in range(remains):
                xi.append(0)
#    print(xi)
    prev = 0
    totalpage = 0
    for i in x:
        totalpage += math.ceil(int(i)/d)
#    print("totalpage = " +str(totalpage))
    for i in range(1,totalpage+1):
        temp = 0    
#        print("pageNumber = " +str(i))
        for j in range(prev,prev+d):
#            print("j= "+str(j))
#            print("xi[j]= "+str(xi[j]))
            if xi[j] == i:
                specialCounter+=1
#                print("Special counter increased !!!___")
            temp = j
#        print("j= "+str(j))
        prev = temp+1
#        print("prev= "+str(prev))
#        print("SpecialCounter = "+str(specialCounter))
#        print("-------------------")
    return specialCounter
    
n,d = map(int , input().split(" "))
arr = list(map(int,input().split(" ")[:n]))
print(special(arr,d,n))