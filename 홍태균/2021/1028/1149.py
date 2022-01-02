'''
RGB거리

'''
import sys
input = sys.stdin.readline

N = int(input())

colors = [list(map(int,input().split())) for _ in range(N)]

# N행 3열로 dp저장
dp = [[0] * 3 for _ in range(N)]

# 처음 집은 바로 저장
dp[0] = colors[0][:]

# 각 색을 선택할 때 가장 작은 값을 저장
# 해당 색을 제외한 나머지 색에서 최소값에 자신의 값을 더하여 저장
for i in range(1,N):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1)%3],dp[i-1][(j+2)%3]) + colors[i][j]

print(min(dp[N-1]))
