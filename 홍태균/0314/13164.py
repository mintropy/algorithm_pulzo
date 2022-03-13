'''
행복 유치원

'''
import sys

input = sys.stdin.readline

N, K = map(int,input().split())
# 키
height = list(map(int,input().split()))
# 차이
diff = [0] * (N-1)
# 차이 저장
for i in range(N-1):
    diff[i] = height[i+1] - height[i]
# 차이 정렬
diff.sort()
# K-1개의 큰값을 제외하고 더한다.
result = sum(diff[:N-K])

print(result)


# INF = 10**9
# dp = [[INF] * 2 for _ in range(2)]

# dp[0][0] = 0
# print(dp)
# for j in range(N-1):
#     for i in range(K):   
#         if dp[i % 2][j] != INF:
#             if dp[i % 2][j+1] > dp[i % 2][j] + height[j+1] - height[j]:
#                 dp[i % 2][j+1] = dp[i % 2][j] + height[j+1] - height[j]
#             if i != K-1 and dp[i+1][j+1] > dp[i % 2][j]:
#                 dp[i+1][j+1] = dp[i % 2][j]

# print(dp)