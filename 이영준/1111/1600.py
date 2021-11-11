"""
Title : 말이 되고픈 원숭이
Link : https://www.acmicpc.net/problem/1600
"""

from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


K = int(input())
W, H = MIIS()

grid = [list(MIIS()) for _ in range(H)]

# 말 이동을 i번 했을 때 방문 위치
visited = [deepcopy(grid) for _ in range(K + 1)]

queue = deque([(0, 0, 0, 0)])

# 말 이동 & 인접 이동
horse_dx = (-2, -1, 1, 2, 2, 1, -1, -2)
dx = (-1, 0, 1, 0)
horse_dy = (1, 2, 2, 1, -1, -2, -2, -1)
dy = (0, 1, 0, -1)
min_count = -1

while queue:
    x, y, count, horse_move = queue.popleft()
    if x == H - 1 and y == W - 1:
        min_count = count
        break
    if visited[horse_move][x][y]:
        continue
    visited[horse_move][x][y] = 1
    if horse_move < K:
        for d in range(8):
            nx, ny = x + horse_dx[d], y + horse_dy[d]
            if 0 <= nx < H and 0 <= ny < W and not visited[horse_move + 1][nx][ny]:
                queue.append((nx, ny, count + 1, horse_move + 1))
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < H and 0 <= ny < W and not visited[horse_move][nx][ny]:
            queue.append((nx, ny, count + 1, horse_move))

print(min_count)

'''
Counter Example
1
5 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 0
ans : 6

3
5 5
0 0 1 1 0
0 1 0 1 0
0 1 1 0 0
0 0 1 1 1
0 0 1 1 0
'''
