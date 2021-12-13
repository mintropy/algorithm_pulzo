"""
Title : 텀 프로젝트
Link : https://www.acmicpc.net/problem/9466
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    students = [0] + list(map(int, input().split()))
    
    check = [0] * (N + 1)
    group = 1
    for i in range(1, N + 1):
        if check[i]:
            continue
        student = students[i]
        # 사이클 찾기
        while not check[student]:
            check[student] = group
            student = students[student]
        # 실제 사이클인 경우만 확인
        while check[student] == group:
            check[student] = -1
            student = students[student]
        group += 1
    
    print(N - check.count(-1))
