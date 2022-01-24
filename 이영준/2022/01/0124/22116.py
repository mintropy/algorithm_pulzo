"""
Title : 창영이와 퇴근
Link : https://www.acmicpc.net/problem/22116
"""

import heapq
import sys
input = sys.stdin.readline


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]


slope = [[-1] * N for _ in range(N)]

heap = [(0, 0, 0)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
while heap:
    s, x, y = heapq.heappop(heap)
    if x == N - 1 and y == N - 1:
        print(s)
        break
    if 0 <= slope[x][y] <= s:
        continue
    slope[x][y] = s
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            diff = max(abs(grid[x][y] - grid[nx][ny]), s)
            if slope[nx][ny] == -1 or diff < slope[nx][ny]:
                heapq.heappush(heap, (diff, nx, ny))
