"""
Title : 박스 나누기 게임
Link : https://www.acmicpc.net/problem/11867
"""

n, m = map(int, input().split())


# 1이면 첫번째 플레이어, 2이면 두번째 플레이어가 승
dp = [[0] * (101) for _ in range(101)]
dp[1][2] = dp[2][1] = 1
# k개 돌을 두 박스로 분배했을 때, 이길 수 있는지
promissing = [False] * 101
promissing[2] = True

# num개 돌을 분배했을 때
for num in range(4, 101):
    # num개 돌을 분배했을 때 이길 수 있는지
    winnable = False
    for i in range(1, num):
        if not promissing[num - i] and not promissing[i]:
            winnable = True
            dp[num - i][i] = 2
        else:
            dp[num - i][i] = 1
    if winnable:
        promissing[num] = True


# 출력
if promissing[n] or promissing[m]:
    print('A')
else:
    print('B')
