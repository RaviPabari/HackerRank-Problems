# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:54:44 2020

@author: Ravi
"""
def removeDups(s):
    for i in s:
        if i=="1":
            s=s.replace("1","",1)
    return s

def reduced(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            s = s.replace(s[i],"1",1)
            s = s.replace(s[i+1],"1",1)
    s = removeDups(s)
    if len(s)==0:
        return "Empty String"
    else:
        return s 

def reduceWithList(s):
    li = list(s)
    i=0
    while i <len(li)-1:
        if li[i]==li[i+1]:
            li.remove(li[i])
            li.remove(li[i])
            i=0
            if len(li)==0:
                return "Empty String"
            else:
                i = i+1
        return "".join(li)

def removeRepeats(S):
    LS = list(S)
    i = 0 
    while i < len(LS)-1:
        if LS[i]==LS[i+1]:
            del LS[i]
            del LS[i]
            i = 0
            if len(LS) == 0:
                print('Empty String')
                break
        else:
            i+=1
    return ''.join(LS)

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:54:44 2020

@author: Ravi
"""
def reducedString(s):
    i = 0
    while len(s)>0:
        if i == len(s)-1:
            return s
        else:
            if s[i] == s[i+1]:
                s = s[:i]+s[i+2:]
                i=0
            else:
                i = i+1
    return "Empty String"

s = input()
print(reducedString(s))     
 

    
            
