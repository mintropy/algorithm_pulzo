"""
Title : 녹색 옷 입은 애가 젤다지?
Link : https://www.acmicpc.net/problem/4485
"""

import heapq
import sys
input = sys.stdin.readline


dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    cave = [list(map(int, input().split())) for _ in range(N)]
    visited = [[N * N * 10] * N for _ in range(N)]
    heap = [(cave[0][0], 0, 0)]
    while heap:
        count, x, y = heapq.heappop(heap)
        if x == N - 1 and y == N - 1:
            print(f'Problem {tc}: {count}')
            break
        if count >= visited[x][y]:
            continue
        visited[x][y] = count
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                heapq.heappush(heap, (count + cave[nx][ny], nx, ny))
    
    tc += 1
