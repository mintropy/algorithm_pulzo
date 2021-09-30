import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

dp = [1]*N
for i in range(1, N):
    tmp = 1
    for j in range(i-1, -1, -1):
        if S[i] > S[j]:
            tmp = max(tmp, 1+dp[j])
        dp[i] = tmp
print(dp)
print(max(dp))