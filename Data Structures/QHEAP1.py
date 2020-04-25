# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 02:34:16 2020

@author: Ravi
"""

arr = []

def max_heapify(arr,n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[l]>arr[largest]:
        largest = l
    else:
        largest = i
    if r<n and arr[r]>arr[largest]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,n,largest)

def min_heapify(arr,n,i):
    minimum = i
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[l]<arr[minimum]:
        minimum = l
    else:
        minimum = i
    if r<n and arr[r]<arr[minimum]:
        minimum = r
    if minimum!=i:
        arr[i],arr[minimum] = arr[minimum],arr[i]
        min_heapify(arr,n,i)
    

def build_max_heap(arr):
    '''
    here we are starting with n/2 because after n/2 i.e. [ n/2+1 ....n]
    all the nodes are leaves , and by definition all leaves are maxheaps
    so there is no need to check them
    '''
    i=len(arr)//2
    n=len(arr)
    while(i>=0):
        max_heapify(arr,n,i)
        i = i-1

def build_min_heap(arr):
    i = len(arr)//2
    n = len(arr)
    while(i>=0):
        min_heapify(arr,n,i)
        i=i-1
        
def heap_sort(arr):
    build_max_heap(arr) #build the max heap first
    for i in range(len(arr)-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        max_heapify(arr,i,0)
        
def insert_into_max(x):
    arr.append(x)
    build_max_heap(arr)

def insert_into_min(x):
    arr.append(x)
    build_min_heap(arr)

def extract_max(x):
    return arr.pop(0)

def extract_min(x):
    return arr.pop(0)

def delete_from_max(x):
    arr.remove(x)
    arr.sort(reverse=True)

def delete_from_min(x):
    arr.remove(x)
    arr.sort()

q = int(input())
for i in range(q):
    x = list(map(int,input().split()))
    if x[0]==1:
       for key in x[1:]:
           insert_into_min(key)
    if x[0]==2:
        for key in x[1:]:
           delete_from_min(key)
    if x[0]==3:
        print(arr[0])    
