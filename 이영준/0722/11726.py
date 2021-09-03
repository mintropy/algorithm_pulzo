'''
Title : 2*n 타일링
Link : https://www.acmicpc.net/problem/11726
'''

import sys

input = sys.stdin.readline

# 신기하게도 피보나치 수열과 같다!
n = int(input())
if n == 1:
    print(1)
else:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    print(dp[-1])