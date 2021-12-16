import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

N = int(input())
arr = list(MIIS())

dp = list([0] * 21 for _ in range(N))  # i번째 숫자까지 계산했을 때, j가 되는 경우의 수(j는 0~20)

dp[0][arr[0]] = 1  # 첫번째 숫자까지 계산했을 때, arr[0]이 되는 경우의 수는 1가지!

for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j]:  # 이전 숫자까지 계산했을 때 경우의 수 있으면
            # 합 가능하면
            if j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]  # 그 수로 갈 수 있는 경우의 수를 더하기

            # 빼기 가능하면
            if j - arr[i] >= 0:
                dp[i][j - arr[i]] += dp[i - 1][j]  # 그 수로 갈 수 있는 경우의 수를 더하기

print(dp[N - 2][arr[-1]])  # 등식
