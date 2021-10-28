import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
edges = [[] for _ in range(N + 1)]
# 인접리스트
for n in range(N - 1):
    n1, n2 = map(int, input().split())
    edges[n1].append(n2)
    edges[n2].append(n1)
d_cnt = g_cnt = 0
# 현재 노드, 부모 노드, 부모 노드와 연결된 노드 개수
queue = deque([[1, 0, 1]])
while queue:
    node, parent, parent_length = queue.popleft()
    # 현재 노드와 연결된 노드 개수
    length = len(edges[node])
    # 리프면 continue
    if length == 1 and node != 1: continue
    # D
    d_cnt += (parent_length - 1) * (length - 1)
    # G
    if length >= 3:
        g_cnt += length * (length - 1) * (length - 2) // 6
    for edge in edges[node]:
        if edge != parent:
            queue.append([edge, node, length])
if d_cnt == 3 * g_cnt:
    print("DUDUDUNGA")
elif d_cnt > 3 * g_cnt:
    print("D")
else:
    print("G")