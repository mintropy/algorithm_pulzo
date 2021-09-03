"""
Title : 나무 위의 벌레
Link : https://www.acmicpc.net/problem/2132
"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(now, f):
    global prob, visited, fruit, tree
    if f in prob:
        prob[f].add(now)
    else:
        prob[f] = {now}
    visited[now] = True
    for p in tree[now]:
        if not visited[p]:
            dfs(p, f + fruit[p])


n = int(input())
fruit = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


# 트리의 지름 찾기
# 1. 지름의 한쪽 끝 찾기
prob = dict()
visited = [False] * (n + 1)
dfs(1, fruit[1])

# 지름의 한쪽 끝 점이 될 수 있는 후보
dia_end = list(prob[max(prob.keys())])

# 지름의 한쪽 끝을 기준으로 지름의 끝 탐색
prob = dict()
for p in dia_end:
    visited = [False] * (n + 1)
    dfs(p, fruit[p])

max_fruite = max(prob.keys())
dia_end += list(prob[max_fruite])
print(max_fruite, min(dia_end))


'''
def dfs(now, l):
    global diameter_points, length, fruit, tree
    if l + fruit[now] > length:
        length = l + fruit[now]
        if length in diameter_points:
            diameter_points[length].append(now)
        else:
            diameter_points[length] = [now]
    visited[now] = True
    for p in tree[now]:
        if not visited[p]:
            dfs(p, l + fruit[now] + fruit[p])


n = int(input())
fruit = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 트리의 지름 찾기
# 원래 문제의 점에서 가중치 대신
# 선분에서의 가중치 문제로 바꾸어 해결
# 가중치는 두 점의 가중치 합으로 설정

# 1. 한 점에서 탐색, 지름의 끝 점 탐색
# 거리-점을 키-값으로 저장, 가장 긴 거리의 점들로 탐색
diameter_points = dict()
length = fruit[1]
visited = [False] * (n + 1)
dfs(1, length)

# 2. 해당 지름 끝 점에서 지름 끝 점 탐색
# 지름의 끝 지점에 여러개가 나오는 경우, 해당 점들로 모두 탐색
# 지름의 끝 점
points = diameter_points[list(diameter_points.keys())[-1]]
min_point = min(points)
diameter_lenght = 3 * 10 ** 9
for p in points:
    diameter_points = dict()
    length = fruit[p]
    visited = [False] * (n + 1)
    dfs(p, length)
    tmp = diameter_points[list(diameter_points.keys())[-1]]
    tmp_min = min(tmp)
    if tmp_min < min_point:
        min_point = tmp_min

print(list(diameter_points.keys())[-1] // 2, min_point)
'''