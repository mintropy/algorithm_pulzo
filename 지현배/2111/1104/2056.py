import sys
# from collections import deque
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N + 1)]
times = [0] * (N + 1)
# indegrees = [0] * (N + 1)
# queue = deque()
# topology = [0] * (N + 1)

for i in range(1, N + 1):
    time, cnt, *prev = map(int, input().split())
    if cnt:
        for p in prev:
            times[i] = max(times[i], time + times[p])
    else:
        times[i] = time
print(max(times))

# for i in range(1, N + 1):
#     time, cnt, *prev = map(int, input().split())
#     times[i] = time
#     if cnt:
#         indegrees[i] = cnt
#         for p in prev:
#             edges[p].append(i)
#     else:
#         queue.append(i)
#         topology[i] = times[i]

# while queue:
#     idx = queue.popleft()
#     for next in edges[idx]:
#         indegrees[next] -= 1
#         topology[next] = max(topology[next], topology[idx] + times[next])
#         if indegrees[next] == 0:
#             queue.append(next)
    
# print(max(topology))