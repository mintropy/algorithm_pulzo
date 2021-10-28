import sys
from collections import deque
input = sys.stdin.readline
def sol():
    N, S, D, F, B, _ = map(int, input().split())
    # 최댓값은 10만으로 잡아주고
    dp = [100000 for _ in range(N + 1)]
    # 경찰서는 -1로 만들어 둔다
    po = list(map(int, input().split()))
    for p in po:
        dp[p] = -1

    # 시작위치 0으로 두고
    X = S
    q = deque([[X, 0]])
    dp[X] = 0
    # BFS
    while q:
        loc, cnt = q.popleft()
        if loc == D:
            return cnt
        if dp[loc] != -1:
            if loc + F <= N and dp[loc + F] > cnt + 1:
                q.append([loc + F, cnt + 1])
                dp[loc + F] = cnt + 1
            if loc - B > 0 and dp[loc - B] > cnt + 1:
                q.append([loc - B, cnt + 1])
                dp[loc - B] = cnt + 1
    return "BUG FOUND"
print(sol())