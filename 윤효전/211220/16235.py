import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = tuple(tuple(map(int, input().split())) for _ in range(N))
board = [[5]*N for _ in range(N)]
tree = tuple([None]*N for _ in range(N))
new_tree = tuple([None]*N for _ in range(N))

for i in range(N):
    for j in range(N):
        tree[i][j] = []
        new_tree[i][j] = deque()

for _ in range(M):
    y, x, z = map(int, input().split())
    y, x = y-1, x-1
    tree[y][x].append(z)
    
for i in range(N):
    for j in range(N):
        tree[i][j] = deque(sorted(tree[i][j]))

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    for i in range(N):
        for j in range(N):
            while tree[i][j]:
                z = tree[i][j].popleft()
                if board[i][j] >= z:
                    board[i][j] -= z
                    new_tree[i][j].append(z+1)
                else:
                    board[i][j] += (z//2)
                    break
            while tree[i][j]:
                z = tree[i][j].popleft()
                board[i][j] += (z//2)
                    
    for i in range(N):
        for j in range(N):
            while new_tree[i][j]:
                z = new_tree[i][j].popleft()
                if z % 5 == 0:
                    for k in range(8):
                        if 0 <= i+dy[k] < N and 0 <= j+dx[k] < N:
                            tree[i+dy[k]][j+dx[k]].appendleft(1)
                tree[i][j].append(z)
                
    for i in range(N):
        for j in range(N):
            board[i][j] += A[i][j]

ans = 0
for i in range(N):
    for j in range(N):   
        ans += len(tree[i][j])

print(ans)