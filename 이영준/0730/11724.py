"""
Title : 연결 요소의 개수
Link : https://www.acmicpc.net/problem/11724
"""

import sys
input = sys.stdin.readline

sys.setrecursionlimit(int(1e6))

def dfs(point):
    global graph, visited
    for q in graph[point]:
        if not visited[q]:
            visited[q] = True
            dfs(q)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
component = 0

for p in range(1, n + 1):
    if not visited[p]:
        visited[p] = True
        component += 1
        dfs(p)

print(component)