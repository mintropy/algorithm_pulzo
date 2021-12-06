"""
Title : 외판원 순회 2
Link : https://www.acmicpc.net/problem/10971
"""

import sys
input = sys.stdin.readline


def TSP(visited: int, current: int) -> int:
    global n, city, dp
    # 모든 도시 순회 완료
    if visited == (1 << n) - 1:
        cost = city[current][0]
        return cost if cost else 1 << (30)
    # 해당 도시에서 방문한 것을 확인 했을 때
    cost = dp[current][visited]
    if cost:
        return cost
    else:
        cost = 1 << (30)
    # 아니라면 탐색
    for i in range(1, n):
        if not (visited & 1 << i):
            move_cost = city[current][i]
            # 다음 도시로 갈 수 있을 때
            if move_cost:
                new_cost = TSP(visited | 1 << i, i)
                if cost > new_cost + move_cost:
                    cost = new_cost + move_cost
    dp[current][visited] = cost
    return dp[current][visited]


n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (1 << n) for _ in range(n)]

print(TSP(1, 0))
