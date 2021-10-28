import sys
from collections import deque
ipt = sys.stdin.readline
def BFS(N, fld, ar):
    chk = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    for i in range(N):
        for j in range(N):
            if chk[i][j] == 0 and ar[i][j] > fld:
                queue = deque([[i, j]])
                cnt += 1
                while queue:
                    y, x = queue.popleft()
                    if chk[y][x] == 0 and ar[y][x] > fld:
                        chk[y][x] = 1
                        for k in range(4):
                            ny = y + dy[k]
                            nx = x + dx[k]
                            if 0 <= ny < N and 0 <= nx < N and chk[ny][nx] == 0 and ar[ny][nx] > fld:
                                queue.append([ny, nx])
    return cnt

def sol():
    N = int(ipt())
    min_height = 100
    area = []
    for _ in range(N):
        tmp = list(map(int, ipt().split()))
        min_height = min(min_height, *tmp)
        area.append(tmp)
    flood = min_height
    max_cnt = 1
    while flood < 100:
        res = BFS(N, flood, area)
        if res == 0:
            break
        max_cnt = max(max_cnt, res)
        flood += 1
    return max_cnt

print(sol())
