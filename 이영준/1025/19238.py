"""
Title : 스타트 택시
Link : https://www.acmicpc.net/problem/19238
"""

import collections
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def find_next_passenger(taxi: tuple) -> tuple:
    global n, taxi_map, passenger, dx, dy
    # 지금 택시 위치에서 bfs탐색으로 가능한 모든 위치까지 거리 구하기
    dist = [[-1] * (n + 1) for _ in range(n + 1)]
    dist[taxi[0]][taxi[1]] = 0
    queue = collections.deque([taxi])
    while queue:
        x, y = queue.popleft()
        dist_now = dist[x][y]
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 1 <= nx <= n and 1 <= ny <= n and not taxi_map[nx][ny] and dist[nx][ny] == -1:
                dist[nx][ny] = dist_now + 1
                queue.append((nx, ny))
    # 각 승객들마다 확인하며 최선의 승객 확인
    min_dist_passenger = -1
    min_dist = n ** 2
    for idx in passenger:
        x, y, *_ = passenger[idx]
        # 해당 위치로 갈 수 있는지
        if dist[x][y] != -1:
            # 최단 거리 & 열, 행 번호 가작 작은지
            if dist[x][y] < min_dist:
                min_dist_passenger = idx
                min_dist = dist[x][y]
            if dist[x][y] == min_dist:
                if passenger[min_dist_passenger][0] > x or (passenger[min_dist_passenger][0] == x and passenger[min_dist_passenger][1] > y):
                    min_dist_passenger = idx
    return min_dist_passenger, min_dist


def transport_passenger(passenger_info: tuple) -> int:
    global n, dx, dy
    st_x, st_y, end_x, end_y = passenger_info
    dist = [[-1] * (n + 1) for _ in range(n + 1)]
    dist[st_x][st_y] = 0
    queue = collections.deque([(st_x, st_y)])
    while queue:
        x, y = queue.popleft()
        # 목적지 도착
        if x == end_x and y == end_y:
            return dist[x][y]
        # 탐색
        dist_now = dist[x][y]
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 1 <= nx <= n and 1 <= ny <= n and not taxi_map[nx][ny] and dist[nx][ny] == -1:
                dist[nx][ny] = dist_now + 1
                queue.append((nx, ny))
    return -1


n, m, fuel = MIIS()

# 인덱스에 맞게 패딩
taxi_map = [[0] * (n + 1)] + [[0] + list(MIIS()) for _ in range(n)]
taxi = list(MIIS())
passenger = {i: tuple(MIIS()) for i in range(m)}

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

while True:
    # 모든 승객을 옮겼을 때
    if not passenger:
        print(fuel)
        break
    # 다음 탑승 승객 확인
    # 해당 승객 위치 까지 이동 비용
    next_passenger, taxi_passenger_dist = find_next_passenger(taxi)
    # 다음 탑승 승객 위치에 가지 못할 때
    if next_passenger == -1:
        print(-1)
        break
    # 해당 승객 목적지 까지 이동 비용
    passenger_target_dist = transport_passenger(passenger[next_passenger])
    # 목적지로 이동하지 못할 때
    if passenger_target_dist == -1:
        print(-1)
        break
    # 연료가 가능한 경우
    if taxi_passenger_dist + passenger_target_dist <= fuel:
        # 연료 사용 & 충전
        fuel -= taxi_passenger_dist + passenger_target_dist
        fuel += passenger_target_dist * 2
        # 해당 승객 제거
        *_, x, y = passenger.pop(next_passenger)
        # 택시 위치 이동
        taxi = [x, y]
    # 연료가 불가능한 경우
    else:
        print(-1)
        break
