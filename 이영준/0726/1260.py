'''
Title : DFS와 BFS
Link : https://www.acmicpc.net/problem/1260
'''

import sys, collections

input = sys.stdin.readline

def dfs(point, visited):
    global graph
    if not visited[point]:
        print(point, end = ' ')
        visited[point] = True
        for p in graph[point]:
            dfs(p, visited)

def bfs(point, visited):
    global graph
    queue = collections.deque([point])
    visited[point] = True
    while queue:
        p = queue.popleft()
        print(p, end = ' ')
        for q in graph[p]:
            if not visited[q]:
                visited[q] = True
                queue.append(q)


n, m, v = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

dfs(v, [False] * (n + 1))
print()
bfs(v, [False] * (n + 1))