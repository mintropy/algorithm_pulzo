import sys, math
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
lines = defaultdict(int)
for i in range(N):
    a, b, _ = map(int, input().split())
    if a == 0:
        b = 1
    if b == 0:
        a = 1
    d = math.gcd(a, b)
    if a < 0:
        d *= -1
    lines[(a // d, b // d)] += 1
s = sum(lines.values())
ans = 0
for line in lines.values():
    s -= line
    ans += line * s
print(ans)