'''
자두나무

'''
import sys
input = sys.stdin.readline

T, W = map(int,input().split())

# 자두 떨어지는 위치
zado_loc = [int(input()) for _ in range(T)]
# 행은 움직이는 횟수
# 열은 시간
dp = [[-1]*T for _ in range(W+1)]

# 처음 시간은 바로 초기화
# 1이면 안움직이는 곳이 1 움직으면 0
if zado_loc[0] == 1:
    dp[0][0] = 1
    dp[1][0] = 0
else:
    dp[0][0] = 0
    dp[1][0] = 1

# 처음 위치
loc = 1
# 시간은 T-1까지
for j in range(T-1):
    # 움직인 횟수를 확인
    for i in range(W+1):
        # -1보다크면 해당 횟수로 움직였다는 뜻
        if dp[i][j] >= 0:
            # 움직인 횟수를 2로 나눈 나머지가 0이면 1에 위치하고 아니면 2에 위치한다
            # 그리고 1을 더하는 것은 나머지가 0,1이기때문

            # 안 움직였을 때
            # 자두가 해당 위치에 떨어지면 +1을 해서 최대값 비교
            if (i % 2) + 1 == zado_loc[j+1]:
                dp[i][j+1] = max(dp[i][j+1],dp[i][j] + 1)
            # 자두가 반대에 떨어지면 자두를 못 얻기 때문에
            else:
                dp[i][j+1] = max(dp[i][j+1],dp[i][j])

            # 범위를 넘는것은 패스
            if i + 1 > W:
                continue
            # 움직였을 때
            if ((i + 1) % 2) + 1 == zado_loc[j+1]:
                dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j] + 1)
            else:
                dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j])

# 마지막 열에서 가장 큰 값이 정답
result = 0
for i in range(W+1):
    if result < dp[i][T-1]:
        result = dp[i][T-1]

print(result)