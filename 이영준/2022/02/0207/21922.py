"""
Title : 학부 연구생 민상
Link : https://www.acmicpc.net/problem/21922
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def rotate(x, y, d, stuff):
    global dx, dy, swap
    if stuff == 1:
        if d in (0, 2):
            return x + dx[d], y + dy[d], d
        else:
            d = (d + 2) % 4
            return x + dx[d], y + dy[d], d
    elif stuff == 2:
        if d in (0, 2):
            d = (d + 2) % 4
            return x + dx[d], y + dy[d], d
        else:
            return x + dx[d], y + dy[d], d
    elif stuff == 3:
        d = swap[0][d]
        return x + dx[d], y + dy[d], d
    else:
        d = swap[1][d]
        return x + dx[d], y + dy[d], d


N, M = MIIS()
lab = [list(MIIS()) for _ in range(N)]
wind_map = [[0] * M for _ in range(N)]

queue = deque([])
for i in range(N):
    for j in range(M):
        if lab[i][j] == 9:
            wind_map[i][j] = 15
            queue.extend([(i, j, d) for d in range(4)])

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
swap = [
    {0: 1, 1: 0, 2: 3, 3: 2},
    {0: 3, 1: 2, 2: 1, 3: 0},
]
while queue:
    x, y, d = queue.popleft()
    if 1<= lab[x][y] <= 4:
        x, y, d = rotate(x, y, d, lab[x][y])
    else:
        x, y = x + dx[d], y + dy[d]
    if 0 <= x < N and 0 <= y < M:
        if not wind_map[x][y] & 1<<d:
            wind_map[x][y] |= 1<<d
            queue.append((x, y, d))

count = 0
for i in range(N):
    for j in range(M):
        if wind_map[i][j]:
            count += 1
print(count)
