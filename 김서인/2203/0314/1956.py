'''
운동
https://www.acmicpc.net/problem/1956
'''

import sys

input = sys.stdin.readline
INF = 401 * 10000

V, E = map(int, input().split())
board = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    start, end, dist = map(int, input().split())
    board[start][end] = dist  # 일방 통행 도로

for i in range(V + 1):  # 자기 자신으로 가는 경우 거리 0
    board[i][i] = 0

# 플로이드 워샬
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

# 도로 길이 합이 가장 작은 사이클!
ans = INF
for i in range(1, V + 1):
    for j in range(1, V + 1):
        if i == j:  # 자기 자신으로 가는 경우는 continue
            continue
        else:
            # 사이클이 있으면
            if board[i][j] != INF and board[j][i] != INF:
                ans = min(ans, board[i][j] + board[j][i])

if ans == INF:
    print(-1)
else:
    print(ans)