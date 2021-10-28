import sys
input = sys.stdin.readline
N = int(input())
# 왼쪽 전봇대 기준으로 정렬
lines = sorted([tuple(map(int, input().split())) for _ in range(N)])
# 오른쪽 전봇대 값을 뽑음
arr = [i for _, i in lines]
dp = [1] + [0 for _ in range(N - 1)]
# 가장 긴 증가 수열의 크기를 구함
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if arr[j] < arr[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(N - max(dp))