'''
Title : 퇴사 2
Link : https://www.acmicpc.net/problem/15486
'''

import sys

input = sys.stdin.readline


n = int(input())
schedule = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 2)

# 마지막 날짜부터 1일까지 거꾸로 DP
for day in range(n, 0, -1):
    duration, wage = schedule[day]
    next_day = day + duration
    # 일 할 수 있는 날짜가 아니면 다음날 값으로 입력
    if next_day > n + 1:
        dp[day] = dp[day + 1]
    else:
        dp[day] = max(dp[day + 1], dp[next_day] + wage)
print(dp[1])