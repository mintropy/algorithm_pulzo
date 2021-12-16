import heapq
import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().strip().split())

INF = 125 * 125 * 9 + 1

tc = 0
while True:
    N = int(input())
    if N == 0:  # 종료
        break

    tc += 1
    cave = []

    for i in range(N):
        tmp = list(MIIS())
        cave.extend(tmp)

    # 다익스트라
    distance = [INF] * (N * N)
    q = []

    # 출발점
    heapq.heappush(q, (cave[0], 0))  # 비용, 위치
    distance[0] = cave[0]

    while q:
        dist, now = heapq.heappop(q)  # 젤 잃는 도둑 루피 적은 지점까지의 비용, 위치
        # 이미 처리되었으면 패스
        if distance[now] < dist:
            continue

        # 그 지점에서 연결된 다른 지점들 비용 업데이트 (상하좌우)
        for k in (-N, N, -1, 1):
            # 옆으로 못 가는 경우..
            if now % N == 0 and k == -1:  # 왼쪽 못가(왼쪽 끝)
                continue
            if (now + 1) % N == 0 and k == 1:  # 오른쪽 못 가(오른쪽 끝)
                continue

            tmp = now + k

            if 0 <= tmp < N * N:  # 범위 확인
                cost = dist + cave[tmp]  # 그 지점 들를 때 비용
                if cost < distance[tmp]:
                    distance[tmp] = cost
                    heapq.heappush(q, (cost, tmp))

    print(f'Problem {tc}: {distance[-1]}')
