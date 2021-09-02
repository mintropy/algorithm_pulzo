import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
vstd0 = [[N * M for _ in range(M)] for _ in range(N)]
vstd1 = [[N * M for _ in range(M)] for _ in range(N)]
di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)
queue = deque()
queue.append([0, 0, 1, 0])
answer = N * M + 1
while queue:
    i, j, cnt, smash = queue.popleft()
    if i == N - 1 and j == M - 1:
        answer = min(answer, cnt)
        break
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if smash == 0:
                if arr[ni][nj] == '0' and vstd0[ni][nj] > cnt + 1:
                    vstd0[ni][nj] = cnt + 1
                    queue.append([ni, nj, cnt + 1, smash])
                if arr[ni][nj] == '1' and vstd1[ni][nj] > cnt + 1:
                    vstd1[ni][nj] = cnt + 1
                    queue.append([ni, nj, cnt + 1, 1])
            elif smash == 1:
                if arr[ni][nj] == '0' and vstd1[ni][nj] > cnt + 1:
                    vstd1[ni][nj] = cnt + 1
                    queue.append([ni, nj, cnt + 1, smash])
print(answer if answer != N * M + 1 else - 1)