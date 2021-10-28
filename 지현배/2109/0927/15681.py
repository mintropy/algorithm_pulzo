import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, R, Q = map(int, input().split())
edges = [[] for _ in range(N + 1)]
answer = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    edges[n1].append(n2)
    edges[n2].append(n1)

def sol(node, parent):
    cnt = 1
    for e in edges[node]:
        if e != parent:
            cnt += sol(e, node)
    answer[node] = cnt
    return cnt

sol(R, 0)
for _ in range(Q):
    print(answer[int(input())])