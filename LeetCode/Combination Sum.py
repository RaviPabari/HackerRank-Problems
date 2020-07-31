#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:57:36 2020

@author: ravi
"""

"""
This a problem of backtracking, link which I used for learning the problem
https://leetcode.com/problems/combination-sum/discuss/752444/Python-clear-explanation-and-intuition-using-combination-with-backtracking-solution

We are given a set of candidate numbers (candidates) (without duplicates) and a
target number (target), find all unique combinations in candidates where the 
candidate numbers sums to target.

Input = candidates = [2,3,6,7], target = 7,
Output :
[
  [7],
  [2,2,3]
]

Input: candidates = [2,3,5], target = 8,
Output :
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

target_path = 7
result = []
arr = [2,3,6,7]

def combination(i,path):
    '''
    this is general combination fun for n size of path
    '''
    # we have found our answer, lets return. 
    #Any code below this statement wont get executed and the recursion stops.
    if len(path)==target_path:
        result.append(path[:])
        print('*'*10)
        print(result)
        print('*'*10)
        return 
    # With each iteration of the for loop, we will reduce the number of 
    # candidates - [1, 2, 3] , [2, 3] , [3]
	# This is important to prevent duplicates.
    for x in range(i, len(arr)):
        #lets keep adding to path.
        path.append(arr[x])
        # lets run combination again, if the path is not our target length, 
        # it will go to the for loop again.
        print('before combination',path)
        combination(x,path)
        print(path)
        # bactrack and remove the last element so that i can move on
        path.pop()
        print(path)
        # print('value of i',x)
        print('-'*20)
def combination_sum(i,path):
    if sum(path)==target_path:
        result.append(path[:])
        return
    if sum(path)>target_path:
        return
    for x in range(i,len(arr)):
        path.append(arr[x])
        combination_sum(x,path)
        path.pop()
    
combination_sum(0,[])
print(result)        