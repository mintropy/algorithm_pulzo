"""
Title : 토마토
Link : https://www.acmicpc.net/problem/7569
"""

import sys, copy
input = sys.stdin.readline


def next_day(tomato: list) -> list:
    global m, n, h, tomato_box, tomato_count
    global dx, dy, dz
    new_tomato = []
    for k, i, j in tomato:
        for d in range(6):
            z, x, y = k + dz[d], i + dx[d], j + dy[d]
            if 0 <= z < h and 0 <= x < n and 0 <= y < m:
                if tomato_box[z][x][y] == 0:
                    tomato_box[z][x][y] = 1
                    new_tomato.append((z, x, y))
                    tomato_count += 1
    return new_tomato


m, n, h = map(int, input().split())

tomato_box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

blank = 0
tomato = []
tomato_count = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato_box[k][i][j] == -1:
                blank += 1
            elif tomato_box[k][i][j] == 1:
                tomato.append((k, i, j))
                tomato_count += 1

dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

day_count = 0

while True:
    new_tomato = next_day(tomato)
    if not new_tomato:
        total = n * m * h
        if tomato_count + blank == total:
            print(day_count)
        else:
            print(-1)
        break
    else:
        day_count += 1
        tomato = new_tomato