# B에 들어가는 것들을 보면서 증가하는 최대 길이를 구하는 문제로 보면 되지 않을까?
# 연결된 전체에서 증가하는 최대 길이를 빼면 답이 나오지 않을까 !

import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
connects = []
for _ in range(n):
    connect = tuple(map(int,input().split()))  # A와 B 연결되는 위치를 튜플로 받아서 리스트에 저장
    connects.append(connect)

# A를 기준으로 정렬
connects.sort()

# B를 보면서 증가하는 최대 길이 구하기
dp = [0] * (n)
for i in range(n):
    for j in range(i):
        if connects[i][1] > connects[j][1]:
            dp[i] = max(dp[i], dp[j]+1)



print(n - max(dp) -1)
