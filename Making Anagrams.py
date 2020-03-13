# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:13:44 2020

@author: Ravi
"""

def NumberOfChar(p,q):
    li = []
    li2 = list(q)
    for i in p:
        if i in li2:
            li.append(i)
            li2.remove(i)
#    return li
    return (len(p)+len(q) - 2*len(li))
p = 'fcrxzwscanmligyxyvym'
q = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
print(NumberOfChar(p,q))