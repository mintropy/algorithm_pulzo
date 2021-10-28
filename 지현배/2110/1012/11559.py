import sys
from collections import deque
dy = (0, 1, 0 ,-1)
dx = (1, 0, -1, 0)
input = sys.stdin.readline
fields = [list(input().rstrip()) for _ in range(12)]
ans = 0
def DFS(y, x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < 12 and 0 <= nx < 6 and visited[ny][nx] and fields[ny][nx] == target:
            visited[ny][nx] = False
            elim_list.append([ny, nx])
            DFS(ny, nx)

while True:
    visited = [[True] * 6 for _ in range(12)]
    isPuyo = False
    # 4개 이상인 뿌요 탐색
    for i in range(11, -1, -1):
        for j in range(6):
            if visited[i][j]:
                target = fields[i][j]
                if target != '.':
                    visited[i][j] = False
                    elim_list = [[i, j]]
                    DFS(i, j)
                    # 연쇄
                    if len(elim_list) > 3:
                        isPuyo = True
                        for y, x in elim_list:
                            fields[y][x] = '.'

    # 뿌요 떨어짐
    for i in range(10, -1, -1):
        for j in range(6):
            if fields[i][j] != '.':
                idx = i
                while idx < 11 and fields[idx + 1][j] == '.':
                    fields[idx + 1][j] = fields[idx][j]
                    fields[idx][j] = '.'
                    idx += 1
    # 종료 조건
    if isPuyo == False:
        break
    else:
        ans += 1
print(ans)

