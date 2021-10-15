"""
Title : 전쟁 - 전투
Link : https://www.acmicpc.net/problem/1303
"""

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
war_map = [input().strip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 우리 나라, 적국의 위력의 합
our_country = enemy_country = 0

# 탐색
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        country = war_map[i][j]
        count = 0
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = True
            count += 1
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and war_map[nx][ny] == country:
                        queue.append((nx, ny))
        if country == 'W':
            our_country += count ** 2
        else:
            enemy_country += count ** 2

print(our_country, enemy_country)
