# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:43:39 2020

@author: Ravi
"""



def caesarCipher(s,k):
    cipherText = ''
    for i in s:
        if i.isalpha():
            a = 'A' if i.isupper() else 'a'
            cipherText += chr( ord(a) +(ord(i)- ord(a)+ k) %26 )
        else:
            cipherText +=i
    return cipherText

n = int(input())
s = input()
k = int(input())
print(caesarCipher(s,k))
