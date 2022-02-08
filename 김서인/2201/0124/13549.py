import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
N, K = map(int, input().split())
q = deque()
distance = [INF] * 200001

if K <= N: # 걸어만 가야 하는 경우
    print(N-K)
else:

    distance[N] = 0
    q.append((N, 0))
    while q:
        idx, cost = q.popleft()

        # 좌우(걸어가기)
        for i in [idx + 1, idx - 1]:
            if 0 <= i <= 200000 and distance[i] > distance[idx] + 1:  # 범위, 방문할지 체크
                distance[i] = distance[idx] + 1
                q.append((i, cost + 1))
        # 점프
        if 0 <= idx * 2 <= 200000 and distance[idx * 2] > distance[idx]:  # 범위, 방문할지 체크
            distance[idx * 2] = distance[idx]
            q.appendleft((idx * 2, cost))

    print(distance[K])
