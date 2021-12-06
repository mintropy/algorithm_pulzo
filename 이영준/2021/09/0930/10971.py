"""
Title : 외판원 순회 2
Link : https://www.acmicpc.net/problem/10971
"""

import sys
input = sys.stdin.readline

def dfs(c: int, city_count: int, cost: int, city_visited: list):
    global n, city, min_cost
    if city_count == n - 1:
        if city[c][0] != 0:
            cost += city[c][0]
            if cost < min_cost:
                min_cost = cost
        return
    for i in range(n):
        if i == c:
            continue
        if city[c][i] == 0:
            continue
        if not city_visited[i]:
            city_visited[i] = True
            cost += city[c][i]
            dfs(i, city_count + 1, cost, city_visited)
            city_visited[i] = False
            cost -= city[c][i]


n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]

# 모든 도시를 순회 >> 원래 도시로 돌아감
# 출발 도시를 어떤 도시로 하던지 상관 없음
min_cost = 10 ** 8

city_visited = [False] * n
city_visited[0] = True

dfs(0, 0, 0, city_visited)

print(min_cost)