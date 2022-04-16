# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 23:22:45 2022

@author: USER
"""

def permutation(s, i, length): #s는 단어리스트, i는 비교하기 위한 수, length는 단어 길이
    if i == length:
        #i가 마지막 길이인 length와 같아지면 각 알파벳을 합친다.
        print(''.join(s), end = ', ') 
    else:
        for j in range(i, length):
            s[i], s[j] = s[j], s[i] #i와 j의 위치를 바꿔준다 
            permutation(s, i+1, length) #다시 permutation을 호출
            s[i], s[j] = s[j], s[i]
        
string = "LANG"
n = len(string)
s = list(string)
permutation(s, 0, n)