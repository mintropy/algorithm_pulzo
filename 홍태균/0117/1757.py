'''
달려달려

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

dist = []
for _ in range(N):
    dist.append(int(input()))

# DP 는 시간을 행으로 열은 지침 지수로 사용
# 지침 지수는 0~M까지 가능하기 때문에 M+1까지
dp = [[-1] * (M+1) for _ in range(N)]
# 초기 시작 
# 처음에 움직이거나 쉬거나
dp[0][0] = 0
dp[0][1] = dist[0]

# 시간에 따라서 시작
# 마지막에는 무조건 쉬어야 하기때문에 N-1까지
for i in range(N-1):
    for j in range(M+1):
        # 도착한 적이 있는 dp이면
        if dp[i][j] != -1:
            # 지침지수가 0
            if j == 0:
                # 안 움직일 때
                if dp[i+1][j] < dp[i][j]:
                    dp[i+1][j] = dp[i][j]
                # 움직인다면 비교하고 더 큰 값.
                # 하지만 열과 행의 합이 N이상이면 마지막에 지침지수가 0일수가 없다.
                if (i + 1) + (j + 1) < N and dp[i+1][j+1] < dp[i][j] + dist[i+1]:
                    dp[i+1][j+1] = dp[i][j] + dist[i+1]
            
            # 지침지수가 M 일때(무조건 쉬어야함)
            # 쉴 때는 무조건 지침지수가 0일때 까지기 때문에
            # 사이는 다 건너뛰고 지침지수가 0 일때 시간에 값을 비교
            elif j == M:
                if dp[i+M][0] < dp[i][j]:
                    dp[i+M][0] = dp[i][j]
            
            # 나머지
            else:
                # 안 움직일 때
                if dp[i+j][0] < dp[i][j]:
                    dp[i+j][0] = dp[i][j]
                # 움직일 때
                if (i + 1) + (j + 1) < N and dp[i+1][j+1] < dp[i][j] + dist[i+1]:
                    dp[i+1][j+1] = dp[i][j] + dist[i+1]
                    
# 지침지수가 0이여야 하기 때문에
print(dp[-1][0])