import collections
import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(list(input().strip()) for _ in range(M))
dir_x, dir_y = [0, 0, -1, 1], [-1, 1, 0, 0]


def bfs(i, j, color):
    cnt = 1

    q = collections.deque()
    visited[i][j] = True
    q.append((i, j))

    while q:
        ii, jj = q.popleft()
        for k in range(4):
            ni = ii + dir_x[k]
            nj = jj + dir_y[k]

            if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == False:  # 범위, 방문 체크
                if arr[ni][nj] == color:
                    cnt += 1
                    visited[ni][nj] = True
                    q.append((ni, nj))
    return cnt ** 2


our_army_power = 0
their_army_power = 0
visited = [[False] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        if visited[i][j] == False:
            power = bfs(i, j, arr[i][j])
            if arr[i][j] == 'W':
                our_army_power += power
            else:
                their_army_power += power

print(our_army_power, their_army_power)
