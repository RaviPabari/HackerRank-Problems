#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:05:20 2020

@author: ravi
"""



for t in range(int(input())):
    s = input()    
    print(s == s[::-1] and "YES" or "NO")