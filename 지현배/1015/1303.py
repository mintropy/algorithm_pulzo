import sys
from collections import deque
input = sys.stdin.readline
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
N, M = map(int, input().split())
battleground = [input().rstrip() for _ in range(M)]
visited = [[True] * N for _ in range(M)]
ally, enemy = 0, 0
for i in range(M):
    for j in range(N):
        if visited[i][j]:
            visited[i][j] = False
            queue = deque([[i, j]])
            target = battleground[i][j]
            cnt = 1
            while queue:
                y, x = queue.popleft()
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < M and 0 <= nx < N and visited[ny][nx] and target == battleground[ny][nx]:
                        visited[ny][nx] = False
                        cnt += 1
                        queue.append([ny, nx])
            else:
                if target == 'W':
                    ally += cnt ** 2
                else:
                    enemy += cnt ** 2
print(ally, enemy)
