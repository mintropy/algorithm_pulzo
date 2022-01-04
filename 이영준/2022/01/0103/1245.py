"""
Title : 농장 관리
Link : https://www.acmicpc.net/problem/1245
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
farm = [tuple(MIIS()) for _ in range(N)]

max_peaks_count = 0
visited = [[False] * M for _ in range(N)]
dx, dy = (-1, -1, -1, 0, 1, 1, 1, 0), (-1, 0, 1, 1, 1, 0, -1, -1)

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        is_peak = True
        h = farm[i][j]
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = True
            for d in range(8):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    if farm[nx][ny] > h:
                        is_peak = False
                    if farm[nx][ny] == h:
                        queue.append((nx, ny))
        if is_peak:
            max_peaks_count += 1

print(max_peaks_count)

'''
3 3
1 1 1
1 1 1
1 1 1
'''