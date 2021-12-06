"""
Title : 레이저빔은 어디로
Link : https://www.acmicpc.net/problem/3709
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
for _ in range(int(input())):
    N, R = MIIS()
    mirrors = set(tuple(MIIS()) for _ in range(R))
    x, y = MIIS()
    
    if x == 0:
        d = 2
    elif x == N + 1:
        d = 0
    elif y == 0:
        d = 1
    elif y == N + 1:
        d = 3
    
    init_x, init_y = x, y
    init_d = d
    x, y = x + dx[d], y + dy[d]
    while True:
        if x == 0 or x == N + 1 or y == 0 or y == N + 1:
            print(x, y)
            break
        if x == init_x and y == init_y and d == init_d:
            print(0, 0)
            break
        if (x, y) in mirrors:
            d = (d + 1) % 4
        x, y = x + dx[d], y + dy[d]
