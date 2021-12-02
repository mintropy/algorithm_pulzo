"""
Title : 벽 부수고 이동하기 4
Link : https://www.acmicpc.net/problem/16946
"""

from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().strip().split())
grid = [list(input().strip()) for _ in range(N)]

places = [0, 0]
place_idx = 2

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

for i in range(N):
    for j in range(M):
        if grid[i][j] == '0':
            count = 0
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                if grid[x][y] == '0':
                    grid[x][y] = place_idx
                    count += 1
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == '0':
                            queue.append((nx, ny))
            places.append(count)
            place_idx += 1

new_grid = []
for i in range(N):
    new_line = []
    for j in range(M):
        if grid[i][j] == '1':
            near_places = set()
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < N and 0 <= ny < M and type(grid[nx][ny]) == int:
                    near_places.add(grid[nx][ny])
            count = 1
            for p in near_places:
                count += places[p]
            new_line.append(count % 10)
        else:
            new_line.append(0)
    new_grid.append(new_line)

for line in new_grid:
    print(*line, sep='')
