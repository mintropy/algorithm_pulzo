import sys
from collections import deque
input = sys.stdin.readline
dy, dx = (1, 0, -1, 0), (0, 1, 0, -1)

N, M, T = map(int, input().split())
castle = [tuple(map(int, input().split())) for _ in range(N)]

fast_way = T + 1

def sol():
    visited = [[True] * M for _ in range(N)]

    queue = deque([[0, 0, 0]])

    while queue:
        global fast_way
        y, x, cnt = queue.popleft()
        if y == N - 1 and x == M - 1:
            return cnt
            
        if cnt > T:
            return -1
        if cnt >= fast_way:
            return -1
            
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] and castle[ny][nx] != 1:
                    visited[ny][nx] = False
                    if castle[ny][nx] == 2:
                        fast_way = abs(N - 1 - ny) + abs(M - 1 - nx) + cnt + 1
                    else:
                        queue.append([ny, nx, cnt + 1])
    else:
        return -1

slow_way = sol()
if fast_way > T:
    if slow_way == -1:
        print('Fail')
    else:
        print(slow_way)
else:
    if slow_way == -1 or slow_way > fast_way:
        print(fast_way)
    else:
        print(slow_way)
