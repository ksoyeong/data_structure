# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

score = []
result = 0 #각 frame의 점수
alltotal = 0 #전체 점수
for i in range(0, 11):
    # a, b 입력받기
    if (i != 10):
        a, b = map(int, input(f"(입력) {i+1} 프레임 : ").split())
    else:
        a, b = map(int, input("(입력) 보너스 프레임 : ").split())
    total = a + b
    # a,b,total 값 가진 리스트 생성
    score.append([a, b, total])
    alltotal += total
    
    # 전에 넘겨온 결과가 spare일 경우 전 점수 변경
    if ( result == 'spare' ) :
        score[i-1][2] += a #이전 점수(total)에 현재 첫번째 값을 더함
        if (i != 10): # 보너스 프레임의 점수는 alltotal에 합산하지 않는다. 앞에서 이미 합산됨
            alltotal += a
        result = 0
    # 전에 넘겨온 결과가 strike일 경우 전 점수 변경
    elif ( result == 'strike' ) :
        score[i-1][2] += total #이전 점수(total)에 현재 첫번째와 두번째 값을 더함
        if(i != 10):
            alltotal += total
        result = 0
        
   # 현재 점수가 strike 혹은 spare인 경우
    if (total == 10):
        result = 'spare'  # 현재 점수의 결과 저장
        if (a == 10 or b == 10) :
            result = 'strike'  # 현재 점수의 결과 저장
            print(f"({a}, {b}, 'X', )")
        else: print(f"({a}, {b}, '/', )")
        print("Total = ", alltotal)
    # 그 외의 경우
    else:
        print(f"({a}, {b}, '-', {total})")
        print("Total = ", alltotal)
        
    # 점수 모두 출력
    for l,m,n in score :
        if (l+m == 10):
            mark = '/'
            if(l == 10 or m == 10 ):
                mark = 'X'
        else: mark = '-'
        
        if (n == 10) : # spare, strike일 경우
            print(f"({score[i][0]}, {score[i][1]}, '{mark}' ,  )", end = "")
        else :
            print(f"({l}, {m}, '{mark}', {n})", end = "")
    print("")