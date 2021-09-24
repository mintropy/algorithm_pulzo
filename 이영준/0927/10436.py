"""
Title : 무한 유리수 트리
Link : https://www.acmicpc.net/problem/10436
"""

import sys
input = sys.stdin.readline
ISS = lambda: input().strip().split()


for _ in range(int(input())):
    tc, value = ISS()
    a, b = map(int, value.split('/'))
    
    # 가장 오른쪽에 있을 때 다음 줄
    if b == 1:
        print(f'{tc} 1/{a + 1}')
    # 바로 위 부모의 오른쪽 자식
    elif a < b:
        print(f'{tc} {b}/{b - a}')
    # 그 외의 경우
    else:
        # 몇 단계 올라가는지
        divisor = (a - b) // b + 1
        # 올라가기
        a -= divisor * b
        # 지금 왼쪽 자식이므로, 올라간 후 오른쪽 자식으로
        a, b = b, b - a
        # 올라온 만큼 왼쪽으로 내려가기
        b += divisor * a
        print(f'{tc} {a}/{b}')
