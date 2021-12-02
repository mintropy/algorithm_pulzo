import sys

input = sys.stdin.readline

INF = 1000 * 1000 * 10
N = int(input())
house_color_costs = list(list(map(int, input().split())) for _ in range(N))

dp = [[0] * 3 for _ in range(2)]  # 각 집이 각 색깔(빨, 초, 파)로 칠해졌을 때의 최소 비용

ans = INF

for k in range(3):  # RGB 각각 시작하는 경우
    # 첫번째 집 칠할 때
    dp[0][0], dp[0][1], dp[0][2] = INF, INF, INF
    dp[0][k] = house_color_costs[0][k]

    for i in range(1, N):  # 두번째 집부터
        dp[1][0] = min(dp[0][1], dp[0][2]) + house_color_costs[i][0]
        dp[1][1] = min(dp[0][0], dp[0][2]) + house_color_costs[i][1]
        dp[1][2] = min(dp[0][0], dp[0][1]) + house_color_costs[i][2]

        dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]

    ans = min(ans, min(dp[0][(k + 1) % 3], dp[0][(k + 2) % 3]))  # 시작한 색깔은 빼고

# 정답
print(ans)
