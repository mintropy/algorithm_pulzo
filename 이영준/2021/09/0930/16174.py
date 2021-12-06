"""
Title : 점프왕 쩰리 (Large)
Link : https://www.acmicpc.net/problem/16174
"""

import sys
imput = sys.stdin.readline
MIIS = lambda: map(int, input().split())

n = int(input())
game_map = [tuple(MIIS()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
visited[0][0] = True

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            num = game_map[i][j]
            if i + num < n:
                visited[i + num][j] = True
            if j + num < n:
                visited[i][j + num] = True

if visited[n - 1][n - 1]:
    print('HaruHaru')
else:
    print('Hing')
