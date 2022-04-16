# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 23:22:45 2022

@author: USER
"""

#튜플의 리스트를 먼저 matrix딕셔너리에 저장
matrix ={(0,1):3, (0,3):2, (1,0):8, (1,2):4, (2,3):5} 

for i in range (3): #행의 수 =3
    for j in range(4): #열의 수 =4 
        #해당하는 key가 없다면, 0을 반환하도록 함
        print(matrix.get((i, j), 0), end = ' ' ) 
    print()