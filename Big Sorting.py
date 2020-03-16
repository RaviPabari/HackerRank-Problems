# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:54:26 2020

@author: Ravi
"""

n = int(input())
unsorted = [input() for _ in range(n)]
unsorted.sort(key = lambda x: (len(x), x))
print('\n'.join(unsorted))
