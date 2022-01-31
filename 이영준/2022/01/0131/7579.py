"""
Title : 앱
Link : https://www.acmicpc.net/problem/7579
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
memory_using = list(MIIS())
operate_cost = list(MIIS())

# i비용으로 얻을 수 있는 최대 메모리
memory_gain = [0] * (10001)

for j in range(N):
    memory = memory_using[j]
    cost = operate_cost[j]
    for i in range(10000, cost - 1, -1):
        if memory_gain[i] < memory_gain[i - cost] + memory:
            memory_gain[i] = memory_gain[i - cost] + memory

for i in range(10001):
    if memory_gain[i] >= M:
        print(i)
        break
