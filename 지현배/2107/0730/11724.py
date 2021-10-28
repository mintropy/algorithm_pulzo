import sys
sys.setrecursionlimit(1100)

N, M = map(int, sys.stdin.readline().split())

arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
chk = [0 for _ in range(N + 1)]
cnt = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    arr[u][v] = 1
    arr[v][u] = 1

def DFS(n):
    chk[n] = 1
    for next_idx in range(1, N + 1):
        if chk[next_idx] == 0 and arr[n][next_idx] == 1:
            DFS(next_idx)

for i in range(1, N + 1):
    if chk[i] == 1:
        continue
    cnt += 1
    DFS(i)
print(cnt)