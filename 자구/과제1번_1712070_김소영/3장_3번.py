# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 23:22:45 2022

@author: USER
"""
def palindrome(word, s, e): #word[s...e] s는 첫번째 자리, e는 마지막 자리
    if (s == e):
        return True
    elif (word[s] != word[e]):
        return False
    elif (s < e+1): 
        return palindrome(word, s+1, e-1)

st = input("단어를 입력하세요 : ")
s = 0
e = len(st)-1 #len은 길이니까 실제 리스트 자리는 1개 빼야한다.
if (palindrome(st, s, e)):
    print("palindrome이 맞습니다.")
else:
    print("palindrome이 아닙니다.")