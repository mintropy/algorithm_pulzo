import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
hx, hy = [-2, -2, -1, 1, 2, 2, -1, 1], [-1, 1, -2, -2, -1, 1, 2, 2]


def bfs():
    q = deque()
    q.append((0, 0, K, 0))  # 맨 왼쪽 위에서 시작 - 인덱스, 말처럼 움직일 기회가 몇번 남았는지, 이동 횟수

    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]  # 세로 좌표, 가로 좌표, 남은 점프 횟수
    visited[0][0][K] = True
    while q:
        i, j, k, cnt = q.popleft()

        # 목적지 도착했으면
        if i == (H - 1) and j == (W - 1):
            return cnt

        # 말처럼 이동 가능하면
        if k > 0:
            for m in range(8):
                ni, nj = i + hx[m], j + hy[m]

                # 범위 체크, 방문 체크, 목적지가 장애물이면 이동 불가능
                if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == 0 and visited[ni][nj][k - 1] == False:
                    visited[ni][nj][k - 1] = True
                    q.append((ni, nj, k - 1, cnt + 1))

        # 사방으로 이동
        for m in range(4):
            ni, nj = i + dx[m], j + dy[m]

            # 범위 체크, 방문 체크, 목적지가 장애물이면 이동 불가능
            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == 0 and visited[ni][nj][k] == False:
                visited[ni][nj][k] = True
                q.append((ni, nj, k, cnt + 1))

    # 도착점 도착할 수 없으면
    return -1


K = int(input())
W, H = map(int, input().split())
arr = tuple(tuple(map(int, input().split())) for _ in range(H))
print(bfs())

'''
1
1 1
0

'''
