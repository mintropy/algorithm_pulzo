import sys
input = sys.stdin.readline
N = int(input())
arr = [[] for _ in range(N)]
maxH = 0
maxTop = []
for i in range(N):
    arr[i] = tuple(list(map(int, input().split())) + [i + 1])
arr.sort()
dp = [[[arr[i][3]], arr[i][1]] for i in range(N)]
for i in range(1, N):
    for j in range(i + 1):
        # i 돌 위에 j 돌 쌓을 수 있을 때
        if arr[i][2] > arr[j][2]:
            # 기존 디피 높이보다 높게 쌓을 수 있으면
            if dp[i][1] < dp[j][1] + arr[i][1]:
                # 디피 갱신
                dp[i][1] = dp[j][1] + arr[i][1]
                dp[i][0] = [*dp[j][0], arr[i][3]]
                # 최댓값 갱신
                if dp[i][1] > maxH:
                    maxH = dp[i][1]
                    maxTop = dp[i][0][:]
# 마지막꺼 하나가 제일 높을 수도 있음
if dp[-1][1] > maxH:
    maxH = dp[i][1]
    maxTop = dp[i][0][:]
print(len(maxTop))
for t in maxTop:
    print(t)