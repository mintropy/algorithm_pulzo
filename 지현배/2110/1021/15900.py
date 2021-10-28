import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
total_depth = 0
def DFS(depth, parent, node):
    isLeaf = True
    for child in edges[node]:
        if child != parent:
            isLeaf = False
            DFS(depth + 1, node, child)
    if isLeaf == True:
        global total_depth
        total_depth += depth

DFS(0, 0, 1)
if total_depth % 2:
    print('Yes')
else:
    print('No')