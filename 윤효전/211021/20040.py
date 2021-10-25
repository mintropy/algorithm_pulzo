import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])

    return parent[node]


def union(v, u):
    root1 = find(v)
    root2 = find(u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


N, M = map(int, input().split())
parent = {i: i for i in range(N)}
rank = dict.fromkeys(parent, 0)
ans = 0
for i in range(1, M+1):
    a, b = map(int, input().split())
    if find(a) == find(b):
        ans = i
        break
    union(b, a)

print(ans)
