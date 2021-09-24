"""
Title : 카드 게임
Link : https://www.acmicpc.net/problem/10835
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


n = int(input())
left = list(MIIS())
right = list(MIIS())

# 왼쪽 i번째 카드, 오른쪽 j번째 카드일 때 점수
dp = [[-1] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            dp[i][j + 1] = -1
            continue
        # 1. 왼쪽 카드만 버리는 경우
        # 2. 두 카드 모두 버리는 경우
        # 3. 오른쪽 카드만 버려서 점수 얻는 경우
        if dp[i + 1][j] < dp[i][j]:
            dp[i + 1][j] = dp[i][j]
        if dp[i + 1][j + 1] < dp[i][j]:
            dp[i + 1][j + 1] = dp[i][j]
        if right[j] < left[i] and dp[i][j + 1] < dp[i][j] + right[j]:
            dp[i][j + 1] = dp[i][j] + right[j]


# 최대 점수 비교
max_score = dp[n][n]
for i in range(n):
    if max_score < dp[n][i]:
        max_score = dp[n][i]
    if max_score < dp[i][n]:
        max_score = dp[i][n]
print(max_score)
