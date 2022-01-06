import sys
import heapq
from collections import deque
input = sys.stdin.readline

def bfs(board, visit, i, j):
    dy = (-1, -1, 0, 1, 1, 1, 0, -1)
    dx = (0, 1, 1, 1, 0, -1, -1, -1)
    dq = deque()
    dq.append((i, j))
    while dq:
        y, x = dq.popleft()
        visit[y][x] = 1
        for i in range(8):
            if y+dy[i] < 0 or y+dy[i] >= len(board) or x+dx[i] < 0 or x+dx[i] >= len(board[0]):
                continue
            if board[y][x] < board[y+dy[i]][x+dx[i]]:
                continue
            if visit[y+dy[i]][x+dx[i]] == 0:
                dq.append((y+dy[i], x+dx[i]))

N, M = map(int, input().split())
board = [tuple(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
h = []
for i in range(N):
    for j in range(M):
        heapq.heappush(h, (-board[i][j], i, j))

ans = 0
while h:
    _, y, x = heapq.heappop(h)
    if visit[y][x] == 0 and board[y][x] != 0:
        ans += 1
        bfs(board, visit, y, x)

print(ans)