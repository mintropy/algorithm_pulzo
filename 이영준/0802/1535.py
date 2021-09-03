"""
Title : 안녕
Link : https://www.acmicpc.net/problem/1535
"""

import sys

n = int(input())
hp_loss = list(map(int, input().split()))
pleasure = list(map(int, input().split()))

dp = [[0] * 102 for _ in range(n)]

for i in range(n):
    hp, pl = hp_loss[i], pleasure[i]
    if i == 0:
        for j in range(hp + 1, 100 + 1):
            dp[i][j] = pl
    else:
        # 해당 친구와 인사하지 못하는 경우
        for j in range(1, hp + 1):
            dp[i][j] = dp[i - 1][j]
        # 인사할 수 있을 때
        for j in range(hp + 1, 100 + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - hp] + pl)

print(dp[-1][-2])


'''
for i in range(n):
    hp, pl = hp_loss[i], pleasure[i]
    # 0 ~ hp 까지는 인사하지 못하므로 그 전 최댓값으로
    for j in range(1, hp + 1):
        if i == 0:
            break
        dp[i][j] = dp[i - 1][j]
    # hp + 1 ~ 100 에서는 최대값으로 갱신
    # 인사했을 때 행복 + 체력 줄었을 때 행복
    # 인사하지 않았을 때(바로 왼쪽칸)
    for j in range(hp + 2, 100 + 1):
        if i == 0:
            dp[i][j] = dp[i][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j - hp] + pl, dp[i - 1][j])

print(dp[-1][-2])
'''