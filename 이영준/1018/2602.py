"""
Title : 돌다리 건너기
Link : https://www.acmicpc.net/problem/2602
"""

import sys
input = sys.stdin.readline


scroll = input().strip()
devil = input().strip()
angel = input().strip()

bridge_len = len(devil)

dp = [[[0] * bridge_len for _ in range(len(scroll))] for _ in range(2)]

# 첫번째 스크롤이 가능한 위치부터 1로 표시
scroll_now = scroll[0]
for j in range(bridge_len):
    if devil[j] == scroll_now:
        for k in range(j, bridge_len):
            dp[0][0][k] += 1
for j in range(bridge_len):
    if angel[j] == scroll_now:
        for k in range(j, bridge_len):
            dp[1][0][k] += 1

# i번째 스크롤을 j번째 밟았을 때
for i in range(1, len(scroll)):
    scroll_now = scroll[i]
    for j in range(i, len(devil)):
        if devil[j] == scroll_now:
            if dp[1][i - 1][j - 1]:
                dp[0][i][j] = dp[1][i - 1][j - 1]
        if angel[j] == scroll_now:
            if dp[0][i - 1][j - 1]:
                dp[1][i][j] = dp[0][i - 1][j - 1]
        dp[0][i][j] += dp[0][i][j - 1]
        dp[1][i][j] += dp[1][i][j - 1]

print(dp[0][-1][-1] + dp[1][-1][-1])
