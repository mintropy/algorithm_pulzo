"""
Title : 총깡 총깡
Link : https://www.acmicpc.net/problem/14618
"""

import sys, collections
input = sys.stdin.readline


n, m = map(int, input().split())
j = int(input())
k = int(input())
a_type = list(map(int, input().split()))
b_type = list(map(int, input().split()))
roads = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    roads[x].append((y, z))
    roads[y].append((x, z))

INF = 10 ** 8
houses = [INF] * (n + 1)

queue = collections.deque([j])
houses[j] = 0
while queue:
    p = queue.popleft()
    dist_p = houses[p]
    for q, dist in roads[p]:
        dist += dist_p
        if dist < houses[q]:
            houses[q] = dist
            queue.append(q)

dist_a = dist_b = INF
for a in a_type:
    if houses[a] < dist_a:
        dist_a = houses[a]
for b in b_type:
    if houses[b] < dist_b:
        dist_b = houses[b]

# 둘 다 불가능한경우
if dist_a == INF and dist_b == INF:
    print(-1)
# 한 종류만 불가능한 경우
elif dist_a == INF:
    print('B')
    print(dist_b)
elif dist_b == INF:
    print('A')
    print(dist_a)
else:
    # 더 짧은 곳으로
    if dist_a <= dist_b:
        print('A')
        print(dist_a)
    else:
        print('B')
        print(dist_b)
