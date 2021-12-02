import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find_parent(x):
    if x == parent[x]:
        return x

    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    parent[find_parent(x)] = find_parent(y)


n, m = map(int, input().split())
parent = list(range(n))

ans = 0
for i in range(1, m + 1):
    x, y = map(int, input().split())
    if find_parent(x) == find_parent(y):
        ans = i
        break
    else:
        union(x, y)

print(ans)
