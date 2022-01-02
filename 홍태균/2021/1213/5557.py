'''
1학년

'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
# 구해야하는 숫자
end = nums[-1]
# 총 (N-1)개의 숫자를 연산하고 0~20까지 숫자이기 때문에
dp = [[0] * 21 for _ in range(N-1)]
# 처음 숫자는 1개있기 때문에
dp[0][nums[0]] = 1

# 각 숫자를 돌아다니기
for i in range(1,N-1):
    # 전의 연산에서 나온 숫자 찾기
    for j in range(21):
        # 0이면 그 숫자가 나올 수 없는 것이기 때문에
        if dp[i-1][j] == 0:
            continue
        # 그전의 숫자 j와 현재 숫자를 더해서 범위 파악
        if 0 <= j + nums[i] <= 20:
            # 범위 안이라면 지금 구한 숫자가 나올 수 있는 경우에서
            # 현재 숫자에서 나올 수 있는 경우의 수를 더한다.
            dp[i][j + nums[i]] += dp[i-1][j]
        # 빼기
        if 0 <= j - nums[i] <= 20:
            dp[i][j - nums[i]] += dp[i-1][j]
# 마지막에 총 연산에서 나올 수 있는 숫자의 등식의 갯수를 알 수 있다.
# 그래서 우리가 원하는 숫자인 end가 나올 수 있는 등식뽑아내기
print(dp[-1][end])


'''
5
1 1 1 1 2
'''