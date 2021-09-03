"""
Title : 회사 문화 1
Link : https://www.acmicpc.net/problem/14267
"""

import sys, collections
input = sys.stdin.readline


n, m = map(int, input().split())
superior = [0] + list(map(int, input().split()))
praise = [tuple(map(int, input().split())) for _ in range(m)]

# 직속 부하, 칭찬
company = [[[], 0] for _ in range(n + 1)]

for i in range(1, n + 1):
    if superior[i] == -1:
        boss = i
        continue
    company[superior[i]][0].append(i)

for i, w in praise:
    company[i][1] += w

queue = collections.deque([boss])
while queue:
    p = queue.popleft()
    for q in company[p][0]:
        company[q][1] += company[p][1]
        queue.append(q)

for i in range(1, n + 1):
    print(company[i][1], end=' ')
