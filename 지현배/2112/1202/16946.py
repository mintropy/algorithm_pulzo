import sys
from collections import deque
input = sys.stdin.readline

dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)

N, M = map(int, input().split())
board = tuple(input().rstrip() for _ in range(N))
visited = [[-1] * M for _ in range(N)]

cnt_arr = []
cnt_idx = -1

for i in range(N):
    for j in range(M):
        if board[i][j] == '0' and visited[i][j] == -1:
            cnt_idx += 1
            visited[i][j] = cnt_idx
            cnt_arr.append(1)
            queue = deque([[i, j]])
            while queue:
                y, x = queue.pop()
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == '0' and visited[ny][nx] == -1:
                        cnt_arr[cnt_idx] += 1
                        visited[ny][nx] = cnt_idx
                        queue.append([ny, nx])
ans = []
for i in range(N):
    tmp = ''
    for j in range(M):
        if board[i][j] == '0':
            tmp += '0'
        else:
            cnt = 1
            tmp_set = set()
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == '0':
                    tmp_set.add(visited[ny][nx])
            for n in tmp_set:
                cnt += cnt_arr[n]
            cnt %= 10
            tmp += str(cnt)
    ans.append(tmp)
print(*ans, sep="\n")