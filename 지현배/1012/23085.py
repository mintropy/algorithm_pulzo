import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
S = input().rstrip()
Tcnt = S.count('T')
cnt_set = set([Tcnt])
queue = deque([[Tcnt, 0]])
ans = -1
while queue:
    T, cnt = queue.popleft()
    if T == N:
        ans = cnt
        break
    for i in range(K + 1):
        # H의 개수가 적으면 패스
        if N - T < K - i:
            continue
        # T의 개수가 적으면 패스
        if T < i:
            break
        # 뒤집기 이후의 T의 개수
        next = T + K - 2 * i
        if not next in cnt_set and 0 <= next <= N:
            cnt_set.add(next)
            queue.append([next, cnt + 1])
print(ans)