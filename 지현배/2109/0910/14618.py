import sys
from heapq import *
input = sys.stdin.readline
N, M = map(int, input().split())
MAX = N * 100 + 1
J = int(input())
K = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
edges = [[] for _ in range(N + 1)]
# 노드별 최솟값
nodes = [MAX for _ in range(N + 1)]
for i in range(M):
    X, Y, Z = map(int, input().split())
    edges[X].append([Y, Z])
    edges[Y].append([X, Z])
H = 'B'
D = MAX
queue = [(0, J)]
while queue:
    dist, node = heappop(queue)
    if dist >= nodes[node]:
        continue
    nodes[node] = dist
    # 거리가 최소보다 멀면 break
    if dist > D:
        break
    # 거리가 같을 때 'A'가 가능하면 'A'
    elif dist == D:
        if H == 'A':
            continue
        if node in A:
            H = 'A'
            continue
    # 아직 A, B를 못 만났으면
    else:
        # A, B집인지 확인
        if node in A:
            H = 'A'
            D = dist
        elif node in B:
            D = dist
        for next, cost in edges[node]:
            heappush(queue, [dist + cost, next])
if D != MAX:
    print(H, D)
else:
    print(-1)