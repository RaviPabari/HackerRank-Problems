#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:17:11 2020

@author: ravi
"""
def panagram(s):
    dict = {}
    s = s.lower()
    for i in range(97,123):
        dict[chr(i)]=0
    for i in s:
        if i in dict:
            dict[i] += 1
        else :
            dict[i] = 1
    val = list(dict.values())
    for i in val:
        if i==0:
            return "not panagram"
    return "panagram"


def pangramSHORTERAF(s):
    s = set(s.lower())#set will sort and remove the dups
    s.discard(" ")
    return 'pangram' if len(s)==26 else 'not pangram'


s = input()
print(pangramSHORTERAF(s))
