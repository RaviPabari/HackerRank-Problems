# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:42:02 2020

@author: Ravi
"""
# book returned on time fine = 0
# 15hackos x days if same month and not returned
# 500hackos x months if same year and not returned
# if not the same year fix 10k Hackos and not returned

def checkFine(d1,m1,y1,d2,m2,y2):
    if(y1==y2):
        if(m1==m2):
            if(d1==d2):
                return 0
            elif(d1 < d2):
                return 0
            else:
                return abs(15*(d2-d1))
        elif(m1 < m2):
            return 0
        else:
            return abs(500*(m2-m1))
    elif(y1 < y2):
        return 0
    else:
        return 10000
        
    
d1,m1,y1 = map(int, input().split())
d2,m2,y2 = map(int , input().split())
print(checkFine(d1,m1,y1,d2,m2,y2))