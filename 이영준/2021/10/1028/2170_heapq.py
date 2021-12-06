import sys, heapq

input = sys.stdin.readline


n = int(input())
lines = []
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(lines, (x, y))

ans = 0
a, b = heapq.heappop(lines)
for _ in range(n - 1):
    x, y = heapq.heappop(lines)
    # 새로 뽑은 선과 겹치지 않을 때
    if b < x:
        ans += b - a
        a, b = x, y
    # 새로 뽑은 선과 겹칠 때
    else:
        b = max(b, y)
ans += b - a
print(ans)