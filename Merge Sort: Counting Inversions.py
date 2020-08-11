# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def merge_lists(left_sublist,right_sublist):
    #augmentaion starts here
    #initialize a inversion count variable to zero
    count_inv = 0
    #initialize both the pointer to zero
    i,j=0,0
    #inititalize empty list in which both the sublists will be merged
    merged_list = []
    
    #iterate through both right and left sublists and compare 
    #and append accordinly to the merged_list
    while(i<len(left_sublist) and j<len(right_sublist)):
        #if the left value is lower than the right value then append the left
        #to the merged_list and increment the left pointer
        if left_sublist[i]<=right_sublist[j]:
            merged_list.append(left_sublist[i])
            i+=1
        else:
            merged_list.append(right_sublist[j])
            j+=1
            #if the right value is added to the merged_list that means 
            #all the remaining values in the left sublist are greater than
            #the current value in the right sublist so just add that count
            #i.e total elements left in left - 1
            count_inv += (len(left_sublist)-i)
    #now add all the remaining elements from left to right
    merged_list += left_sublist[i:]
    merged_list += right_sublist[j:]
    
    #and finally return the merged list with the inversion_count
    return merged_list,count_inv

def merge_sort(main_list):
    #if the list only contains one element return it
    if len(main_list)<=1:
        return main_list,0
    else:
        #splitting the list recursively into sublists and also collecting the 
        #inversion count for the left sublist + right sublist and the middle
        #last splitted array
        midpoint = len(main_list)//2
        (left_sublist,a) = merge_sort(main_list[:midpoint])
        (right_sublist,b) = merge_sort(main_list[midpoint:])
        #return the merged list using the merge_list function
        (sorted_list,c) = merge_lists(left_sublist,right_sublist)
        #simply add all 3 counts and return along the sorted list :)
        return (sorted_list,a+b+c)
#
# input_list = [3,43,4,423,2,34,4,66,1,3,5,76,3,312,312,46]
# sorted_list, inversion_count = merge_sort(input_list)
# print('Sorted list ->',sorted_list)
# print('Inversion count ->',inversion_count)
for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    x,count = merge_sort(arr)
    print(count)
