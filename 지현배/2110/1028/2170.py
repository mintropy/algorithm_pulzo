import sys
input = sys.stdin.readline
N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort(key=lambda x: x[0])
ans = 0
first, last = lines[0][0] - 1, lines[0][0] - 1
for x, y in lines:
    if y > last:
        if last < x:
            ans += last - first
            first = x
        last = y
print(ans + last - first)
