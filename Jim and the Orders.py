# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:03:53 2020

@author: Ravi
"""

#def orders(arr,n):
#    N=n*2
#    dic = {}
#    counter = 0
#    for i in range(0,N,2):
#        sum = 0
#        sum = arr[i]+arr[i+1]
#        dic[counter] = sum
#        counter+=1    
#    ans = []
#    key = list(dic.keys())
#    vals = list(dic.values())
#    dupval = vals[:]
#    for i in range(n):
#        x = min(vals)
#        ind = dupval.index(x)
#        ans.append(key[ind]+1)
#        vals.remove(x)
#    return ans

def orders(arr,n):
    ans = []
    for i , posi in enumerate(arr):
#        print(str(posi))
#        print('i=',str(i))
        ans.append([posi[0]+posi[1], i+1])
    ans.sort()
    service = []
    for i in range(n):
        service.append(ans[i][1])
    return service
n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split(" "))
    arr.append([a,b])
#print(arr)
arr = orders(arr,n)
print(*arr,sep=" ")