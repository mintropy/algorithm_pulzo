"""
Title : 팀 빌딩
Link : https://www.acmicpc.net/problem/22945
"""

import sys
input = sys.stdin.readline

n = int(input())
developers = list(map(int, input().split()))

left, right = 0, n - 1
team_power = 0
while right - left > 1:
    # 팀원 수
    teammates = right - left - 1
    if developers[left] < developers[right]:
        power = developers[left] * teammates
        left += 1
    else:
        power = developers[right] * teammates
        right -= 1
    if power > team_power:
        team_power = power
print(team_power)
