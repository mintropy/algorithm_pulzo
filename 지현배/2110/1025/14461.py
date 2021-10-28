import sys
from heapq import *
dy = (-3, -2, -2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3)
dx = (0, -1, 1, -2, 0, 2, -3, -1, 1, 3, -2, 0, 2, -1, 1, 0)
input = sys.stdin.readline
N, T = map(int, input().split())
grass = [list(map(int, input().split())) for _ in range(N)]
MAX = 0x7fffffff
visited = [[MAX] * N for _ in range(N)]
visited[0][0] = 0
queue = [(0, 0, 0)]
ans = MAX
while queue:
    time, y, x = heappop(queue)
    if y + x >= 2 * N - 4:
        ans = min(ans, time + ((2 * N - 2) - (y + x)) * T)
    for k in range(16):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] > time + 3 * T + grass[ny][nx]:
            visited[ny][nx] = time + 3 * T + grass[ny][nx]
            heappush(queue, (visited[ny][nx], ny, nx))
print(ans)