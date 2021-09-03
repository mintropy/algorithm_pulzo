"""
Title : 쉬운 계단 수
Link : https://www.acmicpc.net/problem/10844
"""

# 끝자리가 해당 숫자로 끝나는 수를 기준으로 개수 확인

from sys import stdin

#n = int(stdin.readline())
n = 1

dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

if n == 1:
    print(9)
else:
    for _ in range(2, n + 1):
        tmp = []
        for i in range(10):
            if i == 0:
                tmp.append(dp[1])
            elif i == 9:
                tmp.append(dp[8])
            else:
                tmp.append(dp[i - 1] + dp[i + 1])
        dp = tmp
    print(sum(dp) % 1000000000)