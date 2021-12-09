"""
Title : 레이저 통신
Link : https://www.acmicpc.net/problem/6087
"""

from collections import deque
import sys
input = sys.stdin.readline


W, H = map(int, input().split())

grid = [list(input().strip()) for _ in range(H)]

pos = []
for i in range(H):
    for j in range(W):
        if grid[i][j] =='C':
            grid[i][j] = '.'
            pos.append((i, j))
st, end = pos

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
visied = [[H * W] * W for _ in range(H)]
visied[st[0]][st[1]] = 0
queue = deque()
for d in range(4):
    nx, ny = st[0] + dx[d], st[1] + dy[d]
    if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.':
        queue.append((0, d, nx, ny))

while queue:
    mirror, d0, x, y = queue.popleft()
    if (x, y) == end:
        print(mirror)
        break
    if visied[x][y] < mirror:
        continue
    visied[x][y] = mirror
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.':
            if d == d0:
                queue.appendleft((mirror, d, nx, ny))
            else:
                queue.append((mirror + 1, d, nx, ny))
