# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:34:03 2020

@author: Ravi
"""

n = input()
n=int(n)
c = 0
alice = 0 
bob = 0
who = True
for i in range(n):
    #for alice true and for bob false
    if who:
        if n>=4:
            alice +=4
            n=n-4
            who = False
        else:
            if n>=1:
                alice +=1
                n=n-1
                who = False
    else:
        if n>=4:
            bob +=4
            n=n-4
            who = True
        else:
            if n>=1:
                bob +=1
                n=n-1
                who = False
if alice == bob:
    if who == False:
        print("Bob")
    else:
        print("Alice")
else:
    if alice > bob:
        print("Alice")
    else:
        print("Bob")
#print('Alice = '+str(alice)+' Bob = '+str(bob))
