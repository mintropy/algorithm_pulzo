"""
Title : 숨바꼭질 3
Link : https://www.acmicpc.net/problem/13549
"""

import collections

n, k = map(int, input().split())

# 더 작은 점 위치에 있는 경우
if k <= n:
    print(n - k)
else:
    queue = collections.deque([n])
    time = [-1] * (10 ** 6 + 1)
    time[n] = 0
    # n보다 큰 점만 탐색 & 100_000 이하만
    while queue:
        pos= queue.popleft()
        if pos == k:
            print(time[pos])
            break
        if pos and pos * 2 <= 10 ** 6 and pos * 2 <= k * 2:
            time[pos * 2] = time[pos]
            queue.appendleft(pos * 2)
        # 한칸 앞 뒤 시간이 -1일때 최신화
        # 뒤로 가지는 않도록
        if pos - 1 >= 0 and time[pos - 1] == -1:
            time[pos - 1] = time[pos] + 1
            queue.append(pos - 1)
        if pos + 1 <= 10 ** 6 and time[pos + 1] == -1:
            time[pos + 1] = time[pos] + 1
            queue.append(pos + 1)
