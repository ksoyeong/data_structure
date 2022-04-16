# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 23:22:45 2022

@author: USER
"""

def harmonic(n):
    if n < 2: #n=1일 경우엔 답이 1
        return 1
    else:
        return 1/n + (harmonic(n-1)) 
        # 1/n + 1/(n-1) + 1/ (n-2)+...이런식으로 더해지도록

num = int(input("n을 입력하세요 : "))
print(harmonic(num))