from collections import Counter

def single1(arr):
    x = Counter(arr)
    for i in x:
        if x[i]==1:
            return i

def single2(arr): 
    """
    Bit manipulation using xor
    example --> any number xored with 0 = the number itself
            --> 7 ^ 0 = 7
            --> 7 ^ 7 = 0
    """
    a = 0
    for i in arr:
        a ^= i
    return a

def single3(arr):
    """
    2*(a+b+c) - (2a+2b+c) == c
    """
    return 2*(sum(set(arr)))-sum(arr)

x = int(input())
arr = list(map(int,input().split()))
print(single(arr))
