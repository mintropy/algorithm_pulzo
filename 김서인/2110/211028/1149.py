import sys

input = sys.stdin.readline

N = int(input())
house_color_costs = list(list(map(int, input().split())) for _ in range(N))

dp = [[0] * 3 for _ in range(N)] # 각 집이 각 색깔(빨, 초, 파)로 칠해졌을 때의 최소 비용
# 첫번째 집 칠할 때
dp[0][0], dp[0][1], dp[0][2] = house_color_costs[0][0], house_color_costs[0][1], house_color_costs[0][2]

# 두번째 집부터
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house_color_costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house_color_costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house_color_costs[i][2]

# 정답
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))
