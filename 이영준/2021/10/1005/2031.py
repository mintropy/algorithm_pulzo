"""
Title : 이 쿠키 달지 않아!
Link : https://www.acmicpc.net/problem/2031
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def bin_search(left: int, right: int, m: int) -> int:
    global foods
    st = left
    st_time = foods[left]
    max_count = 1
    while left <= right:
        mid = (left + right) // 2
        if foods[mid] - st_time >= m:
            right = mid - 1
        else:
            if mid - st + 1 > max_count:
                max_count = mid - st + 1
            left = mid + 1
    return max_count


t, n, d, k = MIIS()
foods = sorted(list(MIIS()))

# 각 시간마다 효과 받는 음식 수
foods_count = [1] * n
for i in range(n):
    foods_count[i] = bin_search(i, n - 1, d)

# i잔을 j번째에 마셨을 때
dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(n):
    foods_now = foods_count[i]
    for j in range(1, k + 1):
        # 해당 차를 마시는지에 대하여
        dp[j][i + foods_now] = max(dp[j][i + foods_now], dp[j - 1][i] + foods_now)
        # 다음 비교할 상태
        dp[j][i + 1] = max(dp[j][i], dp[j][i + 1])

print(dp[k][n])


''''
# WA
for i in range(k):
    for j in range(n):
        # j번 음식 전까지 영향을 받은 음식 수
        if j > 0:
            food_before = dp[i][j]
        else:
            food_before = 0
        # j번 음식에 마시면 효과받는 음식 수
        food_next = foods_count[j]
        if dp[i + 1][j + food_next] < food_before + food_next:
            dp[i + 1][j + food_next] = food_before + food_next
        if j > 0 and dp[i][j] < dp[i][j - 1]:
            dp[i][j] = dp[i][j - 1]

print(max(dp[k]))
'''
