# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:19:02 2020

@author: Ravi
"""

def solve(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year

    


year = int(input())
if ((year < 1918) and (year % 4 == 0)) or \
    ((year > 1918) and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))):
    print('12.09.' + str(year))
elif (year == 1918):
    print('26.09.' + str(year))
else:
    print('13.09.' + str(year))
          