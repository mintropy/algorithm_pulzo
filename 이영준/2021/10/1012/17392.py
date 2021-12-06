"""
Title : 우울한 방학
Link : https://www.acmicpc.net/problem/17392
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

n, m = MIIS()
appointment = list(MIIS())

# 우울해지지 않을 수 있는 최대 일수
total_happiness = sum(appointment) + n

if total_happiness >= m:
    print(0)
else:
    # n일 약속 >> n + 1개 구간
    q, r = divmod(m - total_happiness, n + 1)
    # r일은 연속 q일동안 -1부터 감소
    # n + 1 - r일은 q + 1일동안 감소
    sadness = 0
    for i in range(1, q + 1):
        sadness += (i ** 2) * (n + 1)
    if r != 0:
        sadness += ((q + 1) ** 2) * r
    print(sadness)


'''
Counter Example
2 10
3 2
ans : 3

2 10
2 2
ans : 7

'''