import sys
input = sys.stdin.readline
V, E = map(int, input().split())
edges = sorted([list(map(int, input().split())) for _ in range(E)], key= lambda x: x[2])
parent = [i for i in range(V + 1)]
def find(n):
    if parent[n] == n:
        return n
    p = find(parent[n])
    parent[n] = p
    return p
ans = 0
cnt = 0
for s, e, w in edges:
    if cnt == V - 1:
        break
    if find(s) != find(e):
        parent[find(s)] = find(e)
        cnt += 1
        ans += w
print(ans)