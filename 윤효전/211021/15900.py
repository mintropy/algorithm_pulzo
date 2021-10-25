import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(graph, visit, root):
    ret = 0
    dq = deque()
    dq.append((root, 0))
    while dq:
        node, depth = dq.popleft()
        visit[node] = 1
        can_move = 0
        for to in graph[node]:
            if visit[to] == 0:
                dq.append((to, depth+1))
                can_move += 1
        if can_move == 0:
            ret += depth
    return ret


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (N+1)

total_cnt = bfs(graph, visit, 1)
if total_cnt % 2:
    print('Yes')
else:
    print('No')
