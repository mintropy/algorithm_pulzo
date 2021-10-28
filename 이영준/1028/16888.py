"""
Title : 루트 게임
Link : https://www.acmicpc.net/problem/16888
"""

import sys
input = sys.stdin.readline


dp = [False] * (10 ** 6 + 1)

# 제곱수 먼저 확인
for i in range(1, 10 ** 3 + 1):
    dp[i * i] = True

# 나머지 확인
for i in range(2, 10 ** 6 + 1):
    if not dp[i]:
        # 제곱수를 더하면서 True로 바꿔주기
        for s in range(1, 10 ** 3 + 1):
            if i + s * s >= 10 ** 6:
                break
            dp[i + s * s] = True

for _ in range(int(input())):
    if dp[int(input())]:
        print('koosaga')
    else:
        print('cubelover')
