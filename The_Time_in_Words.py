# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 22:33:03 2020

@author: Ravi
"""

def inWords(a,b):
    c = int(a)
    d = int(b)
    hour = ['one','two','three','four','five','six','seven','eight','nine','ten', 'eleven','twelve','thirteen','fourteen',
            'fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twenty one','twenty two','twenty three',
            'twenty four','twenty five','twenty six','twenty seven','twenty eight', 'twenty nine']
    oclock = "o' clock"
    mini = 'minute'
    adders = ['past','quarter']
    if c ==1 and d ==1:
        return "one minute past one"    
    if b=='00':
        return str(hour[c-1])+" " + oclock
    if c>00 and d<15 :
        temp = str(b)
        temp = str(temp[1])
        temp = int(temp)
        if(temp != 1):
            mini = mini+'s'
        return str(hour[temp-1]) + " " + mini+" "+ adders[0] + " " +str(hour[c-1])
    if d ==15:
        return str(adders[1])+" "+str(adders[0])+" "+str(hour[c-1])

    if d>15 and d<=29:
        return str(hour[d-1])+" "+mini+'s'+" "+ adders[0]+" "+str(hour[c-1])
    
    if d==30:
        return "half"+" "+str(adders[0])+" "+str(hour[c-1])

    if d>30 and d<45:
        xd = 60-d
        return str(hour[xd-1])+" "+mini+'s'+" "+"to"+" "+str(hour[c])
    
    if d==45:
        if c==12:
            c = 0
        return str(adders[1])+" "+"to"+" "+str(hour[c])
    
    if d>45 and d <=59:
        if c == 12:
            c = 0
        xp = 60-d
        if xp!=1:
            mini = mini+'s'
        return str(hour[xp-1])+" "+mini+" "+"to"+" "+str(hour[c])
            
            
        
    
a = input()
b = input()
print(inWords(a,b))
