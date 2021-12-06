"""
Title : 보드게임
Link : https://www.acmicpc.net/problem/2572
"""

import sys
input = sys.stdin.readline

n = int(input())
cards = list(input().strip().split())

m, k = map(int, input().split())
cities = [[] for _ in range(m + 1)]
for _ in range(k):
    a, b, c = input().strip().split()
    a, b = int(a), int(b)
    cities[a].append((b, c))
    cities[b].append((a, c))

# i번째 카드를 냈을 때 j번 마을에 있다면
dp = [[-1] * (m + 1) for _ in range(n + 1)]
dp[0][1] = 0
for i in range(n):
    # 이번 카드의 생상
    color = cards[i]
    # 1번 마을부터 m번 마을까지
    for j in range(1, m + 1):
        # 해당 마을까지 도착했을 때
        cost = dp[i][j]
        if cost >= 0:
            # 해당 마을에서 연결된 마을로 이동 탐색
            for k, c in cities[j]:
                # j >> k 비용과 기존 k마을까지 비용 비교
                if color == c and dp[i + 1][k] < cost + 1:
                    dp[i + 1][k] = cost + 1
                elif color != c and dp[i + 1][k] < cost:
                    dp[i + 1][k] = cost

if max(dp[-1]) == -1:
    print(0)
else:
    print(max(dp[-1]) * 10)


'''
2
G G
3 0

'''