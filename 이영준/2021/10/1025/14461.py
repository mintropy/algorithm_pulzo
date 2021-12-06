"""
Title : 소가 길을 건너는 이유 7
Link : https://www.acmicpc.net/problem/14461
"""

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


n, t = MIIS()
ground = [list(MIIS()) for _ in range(n)]

min_time = 10 ** 10
time_spend = [[min_time for _ in range(n)] for _ in range(n)]

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
# 각 한 칸씩 이동하기 보다, 한번에 3칸씩 이동하는 위치 계산
dx = (-3, -2, -2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3)
dy = (0, -1, 1, -2, 0, 2, -3, -1, 1, 3, -2, 0, 2, -1, 1, 0)

# 위치, 시간, 3번 이동 표시
heap = [(0, 0, 0)]
while heap:
    time, x, y = heapq.heappop(heap)
    # 도착
    if x == n -1 and y == n - 1:
        if time < min_time:
            min_time = time
        continue
    elif (n - 1 - x) + (n - 1 - y) <= 2:
        if time + (n - 1 - x) + (n - 1 - y) < min_time:
            min_time = time + ((n - 1 - x) + (n - 1 - y)) * t
        continue
    # 최단거리로 이동해도 최소 시간보다 느릴 때
    if time + (n - 1 - x + n - 1 - y) * t >= min_time:
        continue
    # 지금 칸에 최단 시간인지
    if time_spend[x][y] < time:
        continue
    time_spend[x][y] = time
    # 탐색
    for d in range(16):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if time + t * 3 + ground[nx][ny] < time_spend[nx][ny]:
                heapq.heappush(heap, (time + t * 3 + ground[nx][ny], nx, ny))

print(min_time)
