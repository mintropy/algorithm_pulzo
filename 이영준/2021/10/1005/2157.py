"""
Title  :여행
Link : https://www.acmicpc.net/problem/2157
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


n, m, k = MIIS()
flights = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b, c = MIIS()
    if a > b:
        continue
    flights[a].append((b, c))

# i번 도시에 j번째로 도착했을 때
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 처음 1번도시 출발 표시
for to, food in flights[1]:
    if dp[to][2] < food:
        dp[to][2] = food

# 남은 도시 순회
for j in range(2, m):
    for i in range(2, n + 1):
        if dp[i][j] > 0:
            happy = dp[i][j]
            for to, food in flights[i]:
                if dp[to][j + 1] < happy + food:
                    dp[to][j + 1] = happy + food

print(max(dp[n]))
