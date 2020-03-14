# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 22:09:11 2020

@author: Ravi
"""

def streak(li):
   head = 0
   tail = 0
   hm = 0
   tm = 0
   for i in li:
       if i == "Heads":
           hm +=1
#           print("hm="+str(hm))
           head = max(head,hm)
#           print("head="+str(head))
       else:
           hm = 0
       if i =="Tails":
           tm +=1
#           print("tm="+str(tm))
           tail = max(tail,tm)
#           print("tail="+str(tail))
       else:
           tm = 0
   print(str(head)+" "+str(tail))
                
        


n = int(input())
li = []
for i in range(n):
    s = input()
    li.append(s)
streak(li)