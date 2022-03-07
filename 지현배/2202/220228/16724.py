import sys
input = sys.stdin.readline

d = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1],
}

N, M = map(int, input().split())
UDLR = []
for _ in range(N):
    UDLR.append(input().rstrip())
zone = [[0] * M for _ in range(N)]
cnt = 0
num = 0

def DFS(n, y, x):
    if 0 <= y < N and 0 <= x < M:
        if zone[y][x] == 0:
            nd = UDLR[y][x]
            zone[y][x] = n
            DFS(n, y + d[nd][0], x + d[nd][1])
        elif zone[y][x] < n:
            global cnt
            cnt -= 1

for i in range(N):
    for j in range(M):
        if zone[i][j] == 0:
            cnt += 1
            num += 1
            DFS(num, i, j)
            
print(cnt)