import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MorW = input().split()
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key= lambda x: x[2])
parent = [i for i in range(N + 1)]

def find(n):
    if parent[n] == n:
        return n
    p = find(parent[n])
    parent[n] = p
    return p

ans = 0
cnt = 0

for u, v, d in edges:
    if cnt == N - 1:
        break
    if find(u) != find(v) and MorW[u - 1] != MorW[v - 1]:
        parent[find(u)] = find(v)
        cnt += 1
        ans += d
if cnt == N - 1:
    print(ans)
else:
    print(-1)