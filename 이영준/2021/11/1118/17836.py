"""
Title : 공주님을 구해라!
Link : https://www.acmicpc.net/problem/17836
"""

import sys, collections
input = sys.stdin.readline

n, m, t = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

# 좌표 두개
queue = collections.deque([(0, 0, 0)])
visited[0][0] = True

# 그람(2)를 얻게되면 최단 경로 계산, 즉시 결과 내기
# 그람을 얻지 못한 경로로 이동했으면, 마지막 칸에 도착하면 정지

direction = {1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}
min_time = 10 ** 6

while queue:
    a, b, l =queue.popleft()
    for i in range(1, 4 + 1):
        x, y = a + direction[i][0], b + direction[i][1]
        if x < 0 or x >= n:
            continue
        if y < 0 or y >= m:
            continue
        if maze[x][y] == 1:
            continue
        if visited[x][y]:
            continue
        if x == n - 1 and y == m - 1:
            if l + 1 < min_time:
                min_time = l + 1
            continue
        if maze[x][y] == 2:
            lenght = l + 1 + (n - 1 - x) + (m - 1 - y)
            if lenght < min_time:
                min_time = lenght
            continue
        queue.append((x, y, l + 1))
        visited[x][y] = True

if min_time <= t:
    print(min_time)
else:
    print('Fail')