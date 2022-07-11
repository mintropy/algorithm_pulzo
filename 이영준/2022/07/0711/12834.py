"""
Title : 주간 미팅
Link : https://www.acmicpc.net/problem/12834
"""

from collections import deque
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

Road = list[list[tuple[int]]]


def search(V: int, start: int, roads: Road) -> list[int]:
    dist = [-1] * (V + 1)
    queue = deque([(start, 0)])
    while queue:
        x, d = queue.popleft()
        if -1 != dist[x] <= d:
            continue
        dist[x] = d
        for y, _d in roads[x]:
            if -1 == dist[y] or dist[y] > d + _d:
                queue.append((y, d + _d))
    return dist


if __name__ == "__main__":
    N, V, E = MIIS()
    A, B = MIIS()
    teammates = list(MIIS())
    roads = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b, l = MIIS()
        roads[a].append((b, l))
        roads[b].append((a, l))
    from_kist = search(V, A, roads)
    from_ssial = search(V, B, roads)
    ans = sum([from_kist[h] + from_ssial[h] for h in teammates])
    print(ans)


"""
KIST 기사단 N명, 장소 V개, 도로 E개

한 사람의 거리 d = (집-kist 최단 거리) + (집-씨앗푸드 최단 거리)
도달할 수 없는 경우 -1
"""
