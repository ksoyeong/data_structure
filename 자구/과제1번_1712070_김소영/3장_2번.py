# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 23:22:45 2022

@author: USER
"""
lst = [3, 28, 34, 200, 13, 20, 65]

def Find_Max(array, l): #array는 리스트, l은 배열의 길이
    if (l==1): #리스트 원소가 하나라면
        return array[0]
    
    max_b = Find_Max(array, l-1) #재귀호출
    if (max_b > array[l-1]):
        return max_b #이전에 나온 재귀함수값
    else:
        return array[l-1]

print(Find_Max(lst, len(lst)))