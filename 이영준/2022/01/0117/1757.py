"""
Title : 달려달려
Link : https://www.acmicpc.net/problem/1757
"""

from copy import deepcopy
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
dist = [int(input()) for _ in range(N)]


dp = [[0] * 2 for _ in range(M + 2)]
dp[1][1] = dist[0]

for i in range(1, N):
    next_dp = [[0] * 2 for _ in range(M + 2)]
    next_dp[0][0] = max(dp[0][0], dp[1][1], dp[1][0])
    next_dp[1][1] = dp[0][0] + dist[i]
    for j in range(1, M):
        next_dp[j][0] = max(dp[j][0], dp[j + 1][1], dp[j + 1][0])
        next_dp[j + 1][1] = dp[j][1] + dist[i]
    dp = deepcopy(next_dp)

print(dp[0][0])


'''
# MLE
N, M = map(int, input().split())
dist = [int(input()) for _ in range(N)]

# i분에 지침지수 j일 때, 달린 상태 k
# M + 2 : for index error
dp = [[[0] * 2 for _ in range(M + 2)] for _ in range(N + 1)]
dp[0][1][1] = dist[0]

for i in range(1, N):
    dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][1][1], dp[i - 1][1][0])
    dp[i][1][1] = dp[i - 1][0][0] + dist[i]
    for j in range(1, M):
        dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j + 1][1], dp[i - 1][j + 1][0])
        dp[i][j + 1][1] = dp[i - 1][j][1] + dist[i]

print(dp[N - 1][0][0])
'''

'''
뛸 수 있는 조건
    이전에 뛰고 있거나, 지침지수가 0일 때
이외의 경우
    쉬었을 때 최대 거리로 갱신
'''

