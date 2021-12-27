import sys
from heapq import *
input = sys.stdin.readline
dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)

t = 1
while True:
    N = int(input())
    if not N: break
    cave = [list(map(int, input().split())) for _ in range(N)]
    MAX = N * N * 10
    visited = [[MAX] * N for _ in range(N)]
    visited[0][0] = cave[0][0]
    queue = [[0, 0, cave[0][0]]]
    while queue:
        y, x, cost = heappop(queue)
        if y == N - 1 and x == N - 1:
            print(f'Problem {t}: {cost}')
            t += 1
            break
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and \
                visited[ny][nx] > cost + cave[ny][nx]:
                visited[ny][nx] = cost + cave[ny][nx]
                heappush(queue, [ny, nx, visited[ny][nx]])