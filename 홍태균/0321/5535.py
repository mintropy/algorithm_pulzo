'''
패셔니스타

'''
import sys
input = sys.stdin.readline

D, N = map(int,input().split())

days = [int(input()) for _ in range(D)]
    
clothes = [list(map(int,input().split())) for _ in range(N)]
clothes.sort(key=lambda x:x[1])

dp = [[0] * N for _ in range(D)]

# 날짜
for i in range(1,D):
    # 해당 날짜
    for j in range(N):
        if clothes[j][0] <= days[i] <= clothes[j][1]:
            # 전 날짜
            for k in range(N):
                if clothes[k][0] <= days[i-1] <= clothes[k][1] and dp[i][j] < dp[i-1][k] + abs(clothes[j][2] - clothes[k][2]):
                    dp[i][j] = dp[i-1][k] + abs(clothes[j][2] - clothes[k][2])

print(max(dp[-1]))