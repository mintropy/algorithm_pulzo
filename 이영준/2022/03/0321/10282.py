"""
Title : 해킹
Link : https://www.acmicpc.net/problem/10282
"""

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


# 944 ms
if __name__ == "__main__":
    for _ in range(int(input())):
        N, D, C = MIIS()
        dependency = [[] for _ in range(N + 1)]
        for _ in range(D):
            a, b, s = MIIS()
            dependency[b].append((a, s))
        heap = [(0, C)]
        total_times = [10 ** 8] * (N + 1)
        total_times[C] = 0
        while heap:
            time, x = heapq.heappop(heap)
            if total_times[x] < time:
                continue
            for y, t in dependency[x]:
                if total_times[y] <= time + t:
                    continue
                total_times[y] = time + t
                heapq.heappush(heap, (time + t, y))
        ans_list = [t for t in total_times if t != 10 ** 8]
        print(len(ans_list), max(ans_list))


# 1140 ms
if __name__ == "__main__":
    for _ in range(int(input())):
        N, D, C = MIIS()
        dependency = [[] for _ in range(N + 1)]
        for _ in range(D):
            a, b, s = MIIS()
            dependency[b].append((a, s))
        heap = [(0, C)]
        count, ans_time = 0, 0
        check = [False] * (N + 1)
        while heap:
            time, x = heapq.heappop(heap)
            if check[x]:
                continue
            check[x] = True
            count += 1
            ans_time = time
            for y, t in dependency[x]:
                if check[y]:
                    continue
                heapq.heappush(heap, (time + t, y))
        print(count, ans_time)
