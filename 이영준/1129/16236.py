"""
Title : 아기 상어
Link : https://www.acmicpc.net/problem/16236
"""

# deque 대신 heap으로 탐색하기
# deque는 넣은 순서대로 탐색하므로, 항상 위, 왼쪽 우선 보장 못함
import sys, heapq

input = sys.stdin.readline

def search(sea, baby_shark, baby_shark_size):
    """
    baby_shark 위치에서 먹을 수 있는 가장 가까운 물고기 탐색
    먹을 수 있는 물고기가 많으면, 가장 위, 왼쪽 기준으로 탐색
    물고기를 먹을 수 있으면, sea에서 물고기 제거, 바뀐 상어 위치 반환
    물고기를 먹을 수 없으면, sea와 baby_shark그대로 반환
    """
    global n
    # 물고기 우선순위 고려, 위, 왼쪽, 오른쪽, 아래 순서로 탐색
    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[baby_shark[0]][baby_shark[1]] = True
    # queue = collections.deque([(baby_shark[0], baby_shark[1], 0)])
    heap = [(0, baby_shark[0], baby_shark[1])]
    # 물고기를 먹었는지
    fish_eaten = False
    # while queue:
    while heap:
        # s1, s2, count = queue.popleft()
        count, s1, s2 = heapq.heappop(heap)
        if 0 < sea[s1][s2] < baby_shark_size:
            sea[s1][s2] = 0
            fish_eaten = True
            break
        for i in range(4):
            x, y = s1 + dx[i], s2 + dy[i]
            if x < 0 or x >= n:
                continue
            if y < 0 or y >= n:
                continue
            # 이미 방문한 경우
            if visited[x][y]:
                continue
            # 항상 위, 왼쪽을 보장할 수 없어서 heap에서 뽑을 때 확인
            # 물고기를 먹을 수 잇는 경우
            # if 0 < sea[x][y] < baby_shark_size:
            #     fish_eaten = True
            #     sea[x][y] = 0
            #     break
            # 더 큰 물고기인 경우
            elif sea[x][y] > baby_shark_size:
                continue
            # 같은 크기이거나, 물고기 없는 경우
            elif sea[x][y] <= baby_shark_size:
                # queue.append((x, y, count + 1))
                heapq.heappush(heap, (count + 1, x, y))
                visited[x][y] = True
    
    if fish_eaten:
        return sea, (s1, s2), count
    else:
        return sea, baby_shark, 0


n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]
total_count = 0
baby_shark_size = 2
baby_shark_eaten_in_size = 0
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            baby_shark = (i, j)
            sea[i][j] = 0

while True:
    # search함수로 나온 new_sea, new_baby_shark 확인
    # baby_shark와 new_baby_shark가 같으면 종료
    new_sea, new_baby_shark, count = search(sea, baby_shark, baby_shark_size)
    # 움직인 횟수가 0이면 종료 == 먹은 물고기 없음
    if count == 0:
        break
    # 움직인 횟수 추가
    total_count += count
    # 상어가 해당 크기에서 먹은 물고기 추가
    baby_shark_eaten_in_size += 1
    # 상어가 해당 크기에서 먹은 물고기 수와 상어 크키가 같을 때
    if baby_shark_eaten_in_size == baby_shark_size:
        baby_shark_size += 1
        baby_shark_eaten_in_size = 0
    baby_shark = new_baby_shark

print(total_count)

'''
# 상어는 가장 가까운 물고기를 먹는다
# 그런 물고기가 여러 마리일 경우 가장 위, 왼쪽 물고기를 먹는다
# 가장 가까운 물고기를 찾고, 가장 위, 왼쪽 물고기를 찾는 방식 필요

from sys import stdin
from collections import deque

# 공간의 크기
n = int(stdin.readline().strip())

# 공간의 상태
graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))
    
# 상어 위치
baby_shark = ()
# 마리수
fish_count = 0
# 물고기 크기별 위치
fish = [[] for _ in range(7)]
for i in range(n):
    for j in range(n):
        num = graph[i][j]
        if num == 9:
            baby_shark = (i, j)
        elif num != 0:
            fish_count += 1
            fish[num].append((i, j))


def bfs(baby_shark, i, j):
    global graph
    queue = deque([(baby_shark[0], baby_shark[1], 0)])
    visited = [[False] * n for _ in range(n)]
    visited[baby_shark[0]][baby_shark[1]] = True
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        a, b, c = queue.popleft()
        for i in range(4):
            na, nb = a + dx[i], b + dy[i]
            if na == i and nb == j:
                graph[na][nb] = 0
                return c + 1
            if na < 0 or na >= n:
                continue
            if nb < 0 or nb >= n:
                continue
            if visited[na][nb]:
                continue
            if graph[na][nb] > baby_shark_size:
                continue
            queue.append((na, nb, c + 1))
            visited[na][nb] = True
    return 0


# 움직인 거리
answer = 0
# 상어 크기
baby_shark_size = 2
# 상어가 해당 크기에서 먹은 물고기 수
fish_eaten = 0
# 먹을 수 있는 물고기
able = []
able.extend(fish[1])
while True:
    # 먹을 수 있는 물고기가 없으면 종료
    if able == []:
        print(answer)
        break
    # 가장 가까운 물고기까지 거리 찾기
    dist = 40
    # 해당 물고기 위치
    target = (21, 21)
    x, y = baby_shark
    for i, j in able:
        # 거리는 bfs로 탐색
        m = bfs(baby_shark, i, j)
        if m == 0:
            continue
        if m < dist:
            dist = m
            target = (i, j)
        # 거리가 같다면 더 위, 왼쪽인지 확인
        elif m == dist:
            if i <= target[0] and j <= target[1]:
                target = (i, j)
    baby_shark = target
    answer += dist
    fish_eaten += 1
    able.remove(target)

    # 상어 크기가 커질 때
    if fish_eaten == baby_shark_size and baby_shark_size <= 6:
        able.extend(fish[baby_shark_size])
        baby_shark_size += 1
        fish_eaten = 0
'''