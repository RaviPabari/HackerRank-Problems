    # -*- coding: utf-8 -*-
    """
    Created on Sun Mar 15 17:26:49 2020
    
    @author: Ravi
    """
    
    def construct(s):
        arr = list(s)
        arr.sort()
        counter = 0
        for i in range(len(arr)-1):
            if arr[i]!=arr[i+1]:
                counter+=1
        return counter
    
    s = input()
    print(construct(s))