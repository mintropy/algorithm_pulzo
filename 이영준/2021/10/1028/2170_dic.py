import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
lines = defaultdict(lambda : -int(1e10))
for _ in range(n):
    x, y = map(int, input().split())
    lines[x] = max(lines[x], y)

start = sorted(lines.keys())
ans = 0
st, end = start[0], lines[start[0]]

for s in start[1:]:
    e = lines[s]
    if s <= end:
        end = max(e, end)
    else:
        ans += end - st
        st, end = s, e
ans += end - st
print(ans)