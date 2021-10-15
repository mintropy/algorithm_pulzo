"""
Title : 자동차경주 
Link : https://www.acmicpc.net/problem/2611
"""

import collections
import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
roads = [[] for _ in range(n + 1)]
roads_in = [0] * (n + 1)
for _ in range(m):
    p, q, r = map(int, input().split())
    roads[p].append((q, r))
    roads_in[q] += 1

# 도시 1번부터 1번 돌아오기까지 위상 정렬
# 각 도시로 들어온 도로 개수 확인
# 위상 정렬
topological_order = []
queue = collections.deque([1])
while queue:
    x = queue.popleft()
    topological_order.append(x)
    for y, _ in roads[x]:
        roads_in[y] -= 1
        if roads_in[y] == 0:
            queue.append(y)

dp = [0] * (n + 1)
dp_last_point = list(range(n + 1))
for pos_now in topological_order[:-1]:
    for pos_next, dist in roads[pos_now]:
        if dp[pos_next] < dp[pos_now] + dist:
            dp[pos_next] = dp[pos_now] + dist
            dp_last_point[pos_next] = pos_now

route = [1]
now = dp_last_point[1]
while now != 1:
    route.append(now)
    now = dp_last_point[now]
route.append(1)

print(dp[1])
print(*route[::-1])
