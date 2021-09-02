"""
Title : ㄷㄷㄷㅈ
Link : https://www.acmicpc.net/problem/19535
"""

import sys, collections
input = sys.stdin.readline


n = int(input())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

# ㅈ개수
g_count = 0
# ㄷ개수
d_count = 0
visited = [False] * (n + 1)
queue = collections.deque([1])
while queue:
    p = queue.popleft()
    if visited[p]:
        continue
    visited[p] = True
    l = len(edges[p])
    # ㅈ 확인
    g_count += (l * (l - 1) * (l - 2)) // 6
    # ㄷ확인
    for q in edges[p]:
        if not visited[q]:
            queue.append(q)
            d_count += (l - 1) * (len(edges[q]) - 1)

g_count *= 3
if d_count == g_count:
    print('DUDUDUNGA')
elif d_count > g_count:
    print('D')
else:
    print('G')


'''
12
1 2
2 3
3 4
2 5
5 6
2 7
2 8
7 9
9 10
8 11
11 12

'''