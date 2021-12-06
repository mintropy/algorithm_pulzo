"""
Title : 휴먼 파이프라인
Link : https://www.acmicpc.net/problem/22981
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

n, k = MIIS()
workers = sorted(list(MIIS()), key=lambda x:-x)

first_team = 1 * workers[0]
second_team = (n - 1) * workers[-1]

for i in range(1, n - 1):
    f = (i + 1) * workers[i]
    s = (n - i - 1) * workers[-1]
    if f + s > first_team + second_team:
        first_team = f
        second_team = s

team_power = first_team + second_team
if k % team_power:
    print(k // team_power + 1)
else:
    print(k // team_power)

'''
Counter Example
4 16
6 5 4 3
ans : 1
'''