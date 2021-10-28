import sys
from collections import deque
input = sys.stdin.readline
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1
L = int(input())
# 방향 변환 정보
query = [0] * L
q_idx = 0
for l in range(L):
    X, C = input().split()
    query[l] = [int(X), C]
# 머리 위치, 몸, 꼬리 위치
y, x = 0, 0
tail = deque([[0, 0]])
board[0][0] = 2
# 방향
d = 0
# 답
cnt = 0
while True:
    cnt += 1
    y += dy[d]
    x += dx[d]
    # 범위를 벗어나거나 자기자신을 만나면 종료
    if not (0 <= y < N and 0 <= x < N) or board[y][x] == 2:
        break
    # 빈곳이면 꼬리를 줄인다
    elif board[y][x] == 0:
        py, px = tail.popleft()
        board[py][px] = 0
    # 진행
    tail.append([y, x])
    board[y][x] = 2
    # 일정 시간에 도달하면 방향을 변환
    if q_idx < L and cnt == query[q_idx][0]:
        if query[q_idx][1] == 'D':
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4
        q_idx += 1
print(cnt)
